import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
from threading import *
import time


class Player:
    """
    Player - Human

    Attributes:
    ----------
    name : str
        Players Name

    Methods:
    ----------
    play(table, other_player)
        :returns 0

    """

    def __init__(self, name):
        self.name = name

    def play(self, table, other_player):
        """
                Attributes:
                ----------
                table: Table()
                    The object that manages the table
                other_player: Player()
                    The other player

                :returns: int
                    The position of the move
        """
        return 0


class EasyComPlayer(Player):
    """
        Player - Computer - easy

        Attributes:
        ----------
        name : str
            Players Name

        Methods:
        ----------
        play(table, other_player)
            What is the move of the player
    """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table , other_player):
        """
        Attributes:
        ----------
        table: Table()
            The object that manages the table
        other_player: Player()
            The other player

        :returns: int
            The position of the move
        """
        return table.random_place()


class NormalComPlayer(Player):
    """
        Player - Computer Normal

        Attributes:
        ----------
        name : str
            Players's Name

        Methods:
        ----------
        play(table, other_player)
            What is the move of the player
       """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table, other_player):
        """
        Checks if the player can win in one move and returns the position
        Checks if the opponent can win in one move and returns the position
        If the central position is free, it returns it
        Checks for a corner position and returns a random corner position
        If none of the above applies, it returns a random position

        Attributes:
        ----------
        table: Table()
            The object that manages the table
        other_player: Player()
            The opponent

        :returns: int
            The position of the move
        """

        if table.ready_to_win(self) is not None:
            return table.ready_to_win(self)
        if table.ready_to_win(other_player) is not None:
            return table.ready_to_win(other_player)
        if table.place_in_center() is not None:
            return 5
        if table.place_in_corner() is not None:
            return table.place_in_corner()
        else:
            return table.random_place()


class HardComPlayer(Player):
    """
        Player - Computer Good

        Attributes:
        ----------
        name : str
            Players's Name

        Methods:
        ----------
        play(table, other_player)
            What is the move of the player
       """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table, other_player):
        """
        Checks if the player can win in one move and returns the position
        Checks if the opponent can win in one move and returns the position
        Checks if it plays first and if so returns a random angle
        If all three positions in a diagonal have been played, check if position 5 is
        occupied by itself and if so returns a middle position
        If the opponent in the third move has two positions in the gammas then he plays one position from the rest
        If the central position is free, it returns it
        Checks for a corner position and returns a random corner position
        If none of the above applies, it returns a random position

        Attributes:
        ----------
        table: Table()
            The object that manages the table
        other_player: Player()
            The opponent

        :returns: int
            The position of the move
        """
        diag = ((1, 5, 9), (3, 5, 7))
        gammas = (
            (1, 2, 3, 6), (2, 3, 6, 9), (3, 6, 9, 8), (6, 9, 8, 7), (9, 8, 7, 4), (8, 7, 4, 1), (7, 4, 1, 2),
            (4, 1, 2, 3))
        if table.ready_to_win(self) is not None:
            return table.ready_to_win(self)
        if table.ready_to_win(other_player) is not None:
            return table.ready_to_win(other_player)
        if len(table.played()) == 0:
            return random.choice([1, 3, 7, 9])
        if len(table.played()) == 3:
            for diagonios in diag:
                if all(j in table.played() for j in diagonios):
                    if 5 in table.tablo[self]:
                        return random.choice([2, 4, 6, 8])
            for gamma in gammas:
                if len(set(gamma).intersection(table.tablo[other_player])) == 2:
                    return random.choice(list(set(gamma).difference(table.tablo[other_player])))
        if table.place_in_center() is not None:
            return 5
        if table.place_in_corner() is not None:
            return table.place_in_corner()
        else:
            return table.random_place()


class ScoreBoard:
    """
    Scoreboard
    keeps track of players' wins and increments the winner's score

    Attributes:
    ----------
    player1 : Player()
        1st player
    player2 : Player()
        2nd player
    board : dict
        Dictionary with player as key and score as data

    Methods:
    ----------
    winner(player)
        Increases the winner's score by 1
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = {player1: 0, player2: 0}

    def winner(self, player):
        """
        Adds the win to the player's score

        Attributes:
        ----------
        player:Player()
            The winner of the game

        :returns: None
        """
        self.board[player] += 1


class Table:
    """
    keep and manage the table of positions played per player.

    Attributes:
    ----------
    player1 : Player()
        1st player
    player2 : Player()
        2nd player
    tablo : dict
        Dictionary with player as key and as data the positions he has played
    winning_series : list
        Table of winning position combinations

    Methods:
    ----------
    place_move(player, number)
        puts the player's move into the dictionary
    played()
        returns a list of the positions that have been played
    toplay()
        returns an array of positions that have not been played
    ready_to_win(player)
        If there is a position that fills a winning column for the player
        returns it otherwise returns None
    place_in_center()
        If the center position is empty it returns it otherwise it returns None
    place_in_corner()
        If there are empty corner positions it returns a random otherwise it returns None
    random_place(self)
        Returns a random position
            """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.tablo = {self.player1: [], self.player2: []}
        self.winning_series = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def place_move(self, player, number):
        """
        Places the player's movement on the table

        Attributes:
        ----------
        player: Player()
            The player who make the move
        number: int
            The position of the move

        :returns:

        """
        self.tablo[player].append(number)

    def played(self):
        """
        returns a list of the positions that have been played

        Attributes:
        ----------
        number: int (1 to 9)
            number indicating the position the player played
        label: Game.label'n'
            the "label" of the position the player played
        game: Game()

        :returns: list
        """
        return self.tablo[self.player1] + self.tablo[self.player2]

    def toplay(self):
        """
        returns a list with the positions that have not been played

        Attributes:
        ----------

       :returns: list
        """
        to_play = []
        for i in range(1, 10):
            if i not in self.played():
                to_play.append(i)
        return to_play

    def ready_to_win(self, player):
        """
        Checks if the given player can win in one move and returns the position

        Attributes:
        ----------
        player: Player()

        :returns: int or None if there is no position that can win
        """
        for winning_no in self.winning_series:
            count = 0
            for number in winning_no:
                if number in self.tablo[player]:
                    count += 1
                if count == 2:
                    if all(number in self.played() for number in winning_no):
                        continue
                    else:
                        for number1 in winning_no:
                            if number1 not in self.played():
                                return number1
        return None

    def place_in_center(self):
        """
        Checks if the center position is empty and returns 5 otherwise returns None

        Attributes:
        ----------

        :returns: 5 or None

        """
        if 5 not in self.played():
            return 5
        else:
            return None

    def place_in_corner(self):
        """
        checks if there are empty corner positions and returns a random one otherwise returns None

        Attributes:
        ----------

        :returns: int or None
        """
        if all(number in self.played() for number in [1, 3, 7, 9]):
            return None
        else:
            while True:
                number = random.choice([1, 3, 7, 9])
                if number not in self.played():
                    return number

    def random_place(self):
        """
        returns a random position

        Attributes:
        ----------

        :returns: int
        """
        return random.choice(self.toplay())


class GameController:
    """
    Game controller

    Attributes:
    ----------
    player1 : Player()
        Player Χ
    player2 : Player()
        Player Ο
    tablo : Table()
        Table object
    score_board : ScoreBoard()
        ScoreBoard object
    game : Game()
        Game object

    count : int
        Move counter
    game_count : int
        Game counter
    couples : int
        1 for human - human, 2 for human - computer, 3 for computer - computer

    Μέθοδοι
    ----------
    get_settings(player1_entry, player2_entry, cd1, cd2, selected_level)
        Checks the type of players and creates the Player1 & Player2 objects
        Creates the tablo & score_board objects
    game_by_couple()
        Checks the pair of players and sets the couples.
        It then creates a Game() object and executes it
    current_player()
        checks the counter and if it is even the player is player1 otherwise player2
    other_player()
        returns the currently not playing player
    new_game()
        changes the counters and clears the table if game_count is not divisible by zero
        sets the count to 1 for the second player to play first
    check_for_winner()
        checks if the currently playing player has filled any winning columns and returns
        True or False
    check_for_draw()
        checks if all seats have been played and if so returns True otherwise False
    click_for_computer()
        Performs the movement of the computer player
    check(number, label)
        It checks the validity of the movement and takes the corresponding actions if it is valid
    color_the_winning_line()
        finds which is the winning row and colors the letters on the labels red
    """

    def __init__(self):
        """
        Initializes GameController fields and creates the main window

        Attributes:
        ----------
        player1 : Player
            creates player object for 1st player
        player2 : Player
            creates player object for the 2nd player
        score_board : ScoreBoard
            creating a score board object
        game : Game
            creating a Game object
        count : int
            variable that counts player moves
        game_count : int
            variable that counts the number of games
        couples : int
            variable characterizing the pair of players:
                1 = human vs human
                2 = human vs computer
                3 = computer vs computer

        """
        self.player1 = None
        self.player2 = None
        self.tablo = None
        self.score_board = None
        self.count = 0
        self.game_count = 0
        self.couples = 0
        app = App(self)
        app.mainloop()

    def get_settings(self, player1_entry, player2_entry, cd1, cd2, selected_level1, selected_level2):
        """
        Checks the type of players and creates the Player1 & Player2 objects
        Creates the tablo & score_board objects

        Attributes:
        __________
        player1_entry: str
            Name of the 1st player
        player2_entry: str
            Name of the 2nd player
        cd1: int (0 or 1)
            0 for human 1 for Computer for the 1st player
        cd2: int (0 or 1)
            0 for human 1 for Computer for the 2nd player
        selected_level1: str
            Easy - Normal - Hard for the 1st player
        selected_level2: str
            Easy - Normal - Hard for the 2nd player

        :returns:
        """
        if cd1 == 0:
            self.player1 = Player(player1_entry)
        else:
            if selected_level1 == "Easy":
                self.player1 = EasyComPlayer(player1_entry + "(ECom)")
            elif selected_level1 == "Normal":
                self.player1 = NormalComPlayer(player1_entry + "(NCom)")
            else:
                self.player1 = HardComPlayer(player1_entry + "(HCom)")
        if cd2 == 0:
            self.player2 = Player(player2_entry)
        else:
            if selected_level2 == "Easy":
                self.player2 = EasyComPlayer(player2_entry + "(ECom)")
            elif selected_level2 == "Normal":
                self.player2 = NormalComPlayer(player2_entry + "(NCom)")
            else:
                self.player2 = HardComPlayer(player2_entry + "(HCom)")
        self.tablo = Table(self.player1, self.player2)
        self.score_board = ScoreBoard(self.player1, self.player2)

    def game_by_couple(self):
        """
        Checks the pair of players and sets the couples.
        It then creates a Game() object and calls the mainloop method

        Attributes:
        __________

        :returns:
        """
        if type(self.player1) == Player and type(self.player2) == Player:
            self.couples = 1
        if type(self.player1) != Player and type(self.player2) != Player:
            self.couples = 3
        else:
            self.couples = 2
        self.game = Game(self)
        self.game.mainloop()

    def current_player(self):
        """
        He checks the counter and if it is even the player is player1 otherwise player2

        Attributes:
        __________

        :returns: Player
        """
        if self.count % 2 == 0:

            return self.player1
        else:
            return self.player2

    def other_player(self):
        """
        Returns the currently not playing player

        Attributes:
        __________

        :returns: Player
        """
        if self.current_player() == self.player1:
            return self.player2
        else:
            return self.player1

    def new_game(self):
        """
        Changes the counters and empties the table if game_count is not divisible by zero
        sets count to 1 for the second player to play first

        Attributes:
        __________

        :returns:
        """
        self.game_count += 1
        self.count = self.game_count % 2
        self.tablo.tablo[self.player1] = []
        self.tablo.tablo[self.player2] = []

    def check_for_winner(self):
        """
        checks if the currently playing player has filled any winning columns and returns True or False

        Attributes:
        __________

        :returns: bool
        """
        for j in self.tablo.winning_series:
            if all(i in self.tablo.tablo[self.current_player()] for i in j):
                return True
        else:
            return False

    def check_for_draw(self):
        """
        checks if all seats have been played and if so returns True otherwise False

        Attributes:
        __________

        :returns: bool
        """

        if len(self.tablo.played()) == 9:
            return True
        else:
            return False

    def click_for_computer(self):
        """
        If 2 computers are playing, it is delayed for 1 second so that the user can catch up with them
        moves on the board
        Checks if the player is human and if not performs the move for the computer player
        """
        if not self.check_for_winner() or not self.check_for_draw():
            if self.couples == 3:
                time.sleep(1)
            play_no = self.current_player().play(self.tablo, self.other_player())
            if play_no != 0:
                eval('self.game.label{}_click("<Button-1>")'.format(play_no))

    def check(self, number, label, game):
        """
        Checks if the selected cell has been played and displays a message.
        If not it checks which player played calls tablo.place_move to place the move on the tablo,
        gives the corresponding text to the label (X or O)
        Checks if there is a winner or a tie and if so:
            1. In case of victory, it registers the victory in the scoreboard and colors the victory column.
            2. Then it calls the open_winner method of the Game object
        if not increment the count change the player name in label_now_plays to show the player who
        has a turn to play and calls the click_for_computer method which if the next player is human waits
        for the user to press a label

        Attributes:
        ----------
        number: int (1 to 9)
            number that indicates the move
        label: Game.label'n'
            the Label object that was clicked
        game: Game()

        :returns:
        """
        if number not in self.tablo.played():
            if self.current_player() == self.player1:
                self.tablo.place_move(self.player1, number)
                label.config(text='X')
            else:
                self.tablo.place_move(self.player2, number)
                label.config(text='O')

            if self.check_for_winner() or self.check_for_draw():
                if self.check_for_winner():
                    self.score_board.winner(self.current_player())
                    self.color_the_winning_line()
                self.game.open_winner()
            else:
                self.count += 1
                game.label_now_plays.config(text="Now Plays: {}".format(self.current_player().name))
                self.click_for_computer()
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to choose an empty place')

    def color_the_winning_line(self):
        """
        It finds which is the winning row and colors the text on the labels to red

        Attributes:
        ----------

        :returns:
        """
        count = 0
        for i in self.tablo.winning_series:
            if all(j in self.tablo.tablo[self.current_player()] for j in i):
                break
            else:
                count += 1
        for k in self.tablo.winning_series[count]:
            eval(f'self.game.label{k}.config(foreground = "red")')


class PlayTwoComputers(Thread):
    """
        Child class of Thread to run code in a separate thread so that it refreshes
        the game window when both players are the computer.

        Attributes:
        ----------
        game: Game()
            The game object
        gc : GameControl()
            The game control object

        Methods:
        ----------
        run()
           Command to run in the Thread
        """

    def __init__(self, game, gc):
        super().__init__()
        self.game = game
        self.gc = gc

    def run(self):
        """
        It replaces the parent's run with the code we want to run in the thread
        which calls the click_for_computer method of the GameController object which
        we created

        Attributes:
        ----------

        :returns:
        """
        self.gc.click_for_computer()


class App(tk.Tk):
    """
        Initial information collection window

        Attributes:
        ----------
        gc : GameController()
            GameController object
        player1_label : ttk.Label
        player1_entry : ttk.Entry
        cd1 : tk.IntVar
        p1_iscom : ttk.Checkbutton
        player2_label : ttk.Label
        player2_entry : ttk.Entry
        cd2 : tk.IntVar
        p2_iscom : ttk.Checkbutton
        selected_level1 : tk.StringVar
        selected_level2 : tk.StringVar
        intell_choise1 : ttk.Combobox
        intell_choise2 : ttk.Combobox
        submit_button : ttk.Button

        Methods:
        ----------
        button_push()
            event when submit_button is pressed
            checks if names have been typed and sets Player1 & Player2 as default and then calls the get_settings method
            of the GameController object where it places the fields we filled in then destroys itself
            and calls game_by_couple() of the game manager object.
    """

    def __init__(self, gc):
        super().__init__()
        self.gc = gc
        self.geometry("+50+50")
        self.title('Tik Tok Toe')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=1)
        # player1
        self.player1_label = tk.Label(self, text="Player1 (X):")
        self.player1_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.player1_entry = ttk.Entry(self)
        self.player1_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # player1 = computer
        self.cd1 = tk.IntVar()
        self.p1_iscom = ttk.Checkbutton(self, text='isComputer', variable=self.cd1)
        self.p1_iscom.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

        # player2
        self.player2_label = ttk.Label(self, text="Player2 (O):")
        self.player2_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.player2_entry = ttk.Entry(self)
        self.player2_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # player2 = computer
        self.cd2 = tk.IntVar()
        self.p2_iscom = ttk.Checkbutton(self, text='isComputer', variable=self.cd2)
        self.p2_iscom.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

        # Computer Intelligence
        self.selected_level1 = tk.StringVar()
        self.selected_level2 = tk.StringVar()
        level = ('Easy', 'Normal', 'Hard')
        self.intell_choise1 = ttk.Combobox(self, textvariable=self.selected_level1, values=level, state='readonly')
        self.intell_choise1.current(0)
        self.intell_choise1.grid(column=3, row=0, sticky=tk.W, padx=(0, 10))
        self.intell_choise2 = ttk.Combobox(self, textvariable=self.selected_level2, values=level, state='readonly')
        self.intell_choise2.current(0)
        self.intell_choise2.grid(column=3, row=1, sticky=tk.W, padx=(0, 10))

        # Submit Button
        submit_button = ttk.Button(self, command=self.button_push, text="Submit")
        submit_button.grid(column=2, row=4, sticky=tk.S, padx=5, pady=5)

    def button_push(self):
        if self.player1_entry.get() == "":
            self.player1_entry.insert(0, "Player1")
        if self.player2_entry.get() == "":
            self.player2_entry.insert(0, "Player2")
        self.gc.get_settings(self.player1_entry.get(), self.player2_entry.get(), self.cd1.get(), self.cd2.get(),
                        self.selected_level1.get(), self.selected_level2.get())

        self.destroy()
        self.gc.game_by_couple()


class Game(tk.Tk):
    """
        Game window
         during initialization it calls the geometry methods (sets the size and position of the window),
         title(literal for window title), resizable(does not allow resizing
         of the window), checks if two computers are playing and if so creates an object
         PlayTwoComputers and calls its run() method.
         If 2 computers are not playing it checks if human is playing and if not it executes the computer's move

        Attributes:
        ----------

        gc : GameController
            object of the GameController class
        camvas : tk.Canvas
           The playing area where the lines will be drawn
        label1 : tk.Label
            label for the upper left position
         label2 : tk.Label
             label for the upper middle position
         label3 : tk.Label
             label for the upper right position
         label4 : tk.Label
             label for the middle left position
         label5 : tk.Label
             label for the central position
         label6 : tk.Label
             label for the middle right position
         label7 : tk.Label
             label for the lower left position
         label8 : tk.Label
             label for the lower middle position
         label9 : tk.Label
             label for the lower right position
        label_now_plays : ttk.Label
             Shows the name of the player that now plays
         score_board_label : tk.Label
             Title for the score
         score_board_p1 : tk.Label
             The name of player1
         score_board_p2 : tk.Label
             The name of player2
         score_board_p1score : tk.Label
             Player1's score
         score_board_p2score : tk.Label
             Player2's score
        on label1, label2, label3, label4, label5, label6, label7, label8, label9 the bind method is
         only activated if at least one player is human so if both players are computer
         not accept movements from the user.
         the labels are placed with coordinates so that they are placed on the camvas and do not cover the lines

        Methods:
        ----------
        open_winner()
            calls TopLevel Winner
        label1_click(event)
            calls the check method of GameController object and executes it with parameters of
            the cell number and the label
         same for each label<x>_click()
       """

    def __init__(self, gc):
        super().__init__()
        self.gc = gc
        self.geometry("+50+50")
        self.title('TikTakToe')
        self.resizable(False, False)

        self.camvas = tk.Canvas(self, width=250, height=215)
        self.camvas.create_line(90, 0, 90, 215, width=4, fill="grey")
        self.camvas.create_line(165, 0, 165, 215, width=4, fill="grey")
        self.camvas.create_line(20, 72, 230, 72, width=4, fill="grey")
        self.camvas.create_line(20, 142, 230, 142, width=4, fill="grey")
        self.camvas.grid(column=0, columnspan=2, row=0, pady=(10, 20))
        self.label1 = tk.Label(self.camvas, text="", font=("Arial", 40), width=2)
        self.label1.place(x=20, y=2, width=65, height=65)
        if self.gc.couples != 3:
            self.label1.bind("<Button-1>", self.label1_click)
        self.label2 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label2.place(x=95, y=2, width=65, height=65)
        if self.gc.couples != 3:
            self.label2.bind("<Button-1>", self.label2_click)
        self.label3 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label3.place(x=170, y=2, width=65, height=65)
        if self.gc.couples != 3:
            self.label3.bind("<Button-1>", self.label3_click)
        self.label4 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label4.place(x=20, y=74, width=65, height=65)
        if self.gc.couples != 3:
            self.label4.bind("<Button-1>", self.label4_click)
        self.label5 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label5.place(x=95, y=74, width=65, height=65)
        if gc.couples != 3:
            self.label5.bind("<Button-1>", self.label5_click)
        self.label6 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label6.place(x=170, y=74, width=65, height=65)
        if gc.couples != 3:
            self.label6.bind("<Button-1>", self.label6_click)
        self.label7 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label7.place(x=20, y=146, width=65, height=65)
        if gc.couples != 3:
            self.label7.bind("<Button-1>", self.label7_click)
        self.label8 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label8.place(x=95, y=146, width=65, height=65)
        if gc.couples != 3:
            self.label8.bind("<Button-1>", self.label8_click)
        self.label9 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label9.place(x=170, y=146, width=65, height=65)
        if gc.couples != 3:
            self.label9.bind("<Button-1>", self.label9_click)
        self.label_now_plays = tk.Label(self, font=("Arial", 15), width=30)
        self.label_now_plays.config(text="Now Plays: {}".format(self.gc.current_player().name))
        self.label_now_plays.grid(column=0, columnspan=2, row=1, padx=(0, 0), sticky=tk.N)
        self.camvas_line1 = tk.Canvas(self, width=250, height=10)
        self.camvas_line1.create_line(0, 5, 250, 5, width=2, fill="grey")
        self.camvas_line1.grid(column=0, columnspan=2, row=2, pady=(5, 5))
        self.score_board_label = tk.Label(self, anchor="center", text="Score",
                                          font=("Arial", 15), width=15)
        self.score_board_label.grid(column=0, columnspan=2, row=3, sticky=tk.NSEW, padx=(0, 0), pady=(10, 0))

        self.label_x = tk.Label(self, borderwidth=2, text="X", font=("Arial", 20), width=1)
        self.label_x.grid(column=0, row=4, padx=(0, 0))
        self.label_y = tk.Label(self, borderwidth=2, text="O", font=("Arial", 20), width=1)
        self.label_y.grid(column=1, row=4, padx=(0, 0))
        self.score_board_p1 = tk.Label(self, borderwidth=2, text=f"{self.gc.player1.name}",
                                       font=("Arial", 12), width=20)
        self.score_board_p1.grid(column=0, row=5, padx=(0, 0))
        self.score_board_p2 = tk.Label(self, text=f"{self.gc.player2.name}", font=("Arial", 12), width=20)
        self.score_board_p2.grid(column=1, row=5, padx=(0, 0))
        self.camvas_line2 = tk.Canvas(self, width=250, height=10)
        self.camvas_line2.create_line(0, 5, 250, 5, width=2, fill="grey")
        self.camvas_line2.grid(column=0, columnspan=2, row=6, pady=(5, 5))
        self.score_board_p1score = tk.Label(self, text=f"{self.gc.score_board.board[self.gc.player1]}",
                                            font=("Arial", 15), width=8)
        self.score_board_p1score.grid(column=0, row=7, pady=(2, 30))
        self.score_board_p2score = tk.Label(self, text=f"{self.gc.score_board.board[self.gc.player2]}",
                                            font=("Arial", 15), width=8)
        self.score_board_p2score.grid(column=1, row=7, pady=(2, 30))

        # αν οι αντίπαλοι είναι δύο υπολογιστές δημιουργεί ένα Thread αντικείμενο (autoplay)
        # και καλεί τη start του αντικειμένου ώστε να εκτελεστούν οι κινήσεις χωρίς να διακοπεί η
        # επανάληψη του παραθύρου και να μπορούμε να της βλέπουμε τις κινήσεις στην οθόνη.
        if self.gc.couples == 3:
            autoplay = PlayTwoComputers(self, self.gc)
            autoplay.start()
        # διαφορετικά αν ο παίκτης που παίζει είναι υπολογιστής καλεί τη μέθοδο play του παίχτη και
        # καλεί την bind του αντίστοιχου label.
        elif self.gc.current_player().play(self.gc.tablo, self.gc.other_player()) != 0:
            eval('self.label{}_click("<Button-1>")'.format(self.gc.current_player().play(self.gc.tablo, self.gc.other_player())))

    def open_winner(self):
        Winner(self.gc)

    def label1_click(self, event):
        self.gc.check(1, self.label1, self)

    def label2_click(self, event):
        self.gc.check(2, self.label2, self)

    def label3_click(self, event):
        self.gc.check(3, self.label3, self)

    def label4_click(self, event):
        self.gc.check(4, self.label4, self)

    def label5_click(self, event):
        self.gc.check(5, self.label5, self)

    def label6_click(self, event):
        self.gc.check(6, self.label6, self)

    def label7_click(self, event):
        self.gc.check(7, self.label7, self)

    def label8_click(self, event):
        self.gc.check(8, self.label8, self)

    def label9_click(self, event):
        self.gc.check(9, self.label9, self)


class Winner(tk.Toplevel):
    """
        Toplevel Win or Draw Window
        on initialization it calls grab_set() so that the user cannot make any move to
        Game Window

        Attributes:
        ----------
        gc : GameControl
            GameControl object
        label_winner : tk.Label
            Displays the title Win or Draw
        label_winner_name : tk.Label
            If we have a winner, it shows their name
        label_score : tk.Label
            Title for the score
        label_p1 : tk.Label
            Name of player1
        label_p2 : tk.Label
            Name of player2
        label_score_p1 : tk.Label
            Player1's score
        label_score_p2 : tk.Label
            Player2's score
        button_continue : tk.Label
            Button to continue the game
        button_end : tk.Label
            Button to end the game

        Methods:
        ----------
        create_widgets()
            creates the window elements
        button_continue_push()
            calls new_game() from the GameController object we created
            calls grap_release() to release the Game Window
            it crashes the Game Window
            and calls game_by_couple() from the GameController object we created
        button_end_push()
            it crashes the Game Window
       """

    def __init__(self, gc):
        self.gc = gc
        super().__init__()
        self.geometry("+400+350")
        self.title('TikTakToe')
        self.grab_set()
        self.resizable(False, False)
        # Ελέγχει αν υπάρχει νικητής ή είναι ισοπαλία το game και εμφανίζει το ανάλογο label
        # και το όνομα του νικητή αν υπάρχει
        if self.gc.check_for_winner():
            self.label_winner = tk.Label(self, text="The winner is:",
                                         font=("Arial", 13))
            self.label_winner.grid(column=0, row=0)
            self.label_winner_name = tk.Label(self, text=f"{self.gc.current_player().name}", font=("Arial", 19),
                                              width=24)
            self.label_winner_name.grid(column=0, columnspan=2, row=1)
        else:
            self.label_winner = tk.Label(self, text="The Game is DRAW", font=("Arial", 15), width=30)
        self.label_winner.grid(column=0, columnspan=2, row=0)
        self.camvas_line = tk.Canvas(self, width=250, height=10)
        self.camvas_line.create_line(0, 5, 250, 5, width=2, fill="grey")
        self.camvas_line.grid(column=0, columnspan=2, row=2, pady=(5, 5))
        self.label_score = tk.Label(self, text="Score", font=("Arial", 17), width=12)
        self.label_score.grid(column=0, columnspan=2, row=3, pady=(20, 0))
        self.label_p1 = tk.Label(self, text=f"{gc.player1.name}", font=("Arial", 13), width=24)
        self.label_p1.grid(column=0, row=4)
        self.label_p2 = tk.Label(self, text=f"{gc.player2.name}", font=("Arial", 13), width=24)
        self.label_p2.grid(column=1, row=4)
        self.label_score_p1 = tk.Label(self, text=f"{gc.score_board.board[gc.player1]}", font=("Arial", 17), width=3)
        self.label_score_p1.grid(column=0, row=5)
        self.label_score_p2 = tk.Label(self, text=f"{gc.score_board.board[gc.player2]}", font=("Arial", 17), width=3)
        self.label_score_p2.grid(column=1, row=5)
        self.button_continue = ttk.Button(self, command=self.button_continue_push, text="Continue")
        self.button_continue.grid(column=0, row=6, padx=1, pady=20)
        self.button_end = ttk.Button(self, command=self.button_end_push, text="End")
        self.button_end.grid(column=1, row=6, padx=1, pady=20)
        # αν κλείσει ο χρήστης το παράθυρο από το x να κλείσει και το Game παράθυρο για να
        # μην κάνει έξτρα κινήσεις
        self.protocol("WM_DELETE_WINDOW", self.button_end_push)

    def button_continue_push(self):
        self.gc.new_game()
        self.grab_release()
        self.gc.game.destroy()
        self.gc.game_by_couple()

    def button_end_push(self):
        self.gc.game.destroy()


if __name__ == "__main__":
    gc = GameController()
