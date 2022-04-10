import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random


# Class human player
class Player():

    def __init__(self, name):
        self.name = name

    def play(self):
        print("human")


# Class Computer Easy player
class EasyComPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def play(self):
        print("easycom")


# Class Computer Normal player
class NormalComPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def play(self):
        print("normalcom")


# Class που κρατάει το σκορ των νικών των παιχτών
class ScoreBoard():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = {player1: 0, player2: 0}

    # μέθοδος για την προσθήκη νίκης στο
    def winner(self, player):
        self.board[player] += 1


# Class που κρατάει τον πίνακα των θέσεων που έχουν παιχτεί αν παίκτη.
class Table():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.tablo = {self.player1: [], self.player2: []}

    # Τοποθετεί την επιλογή στο λεξικό
    def place_move(self, player, number):
        self.tablo[player].append(number)

    # Επιστρέφει list με τους παιγμένους αριθμούς
    def played(self):
        return self.tablo[self.player1] + self.tablo[self.player2]

    # Επιστρέφει αριθμό (για νίκη ή μπλοκάρισμα νίκης) ή None αν δεν υπάρχει
    def ready_to_win(self, player):
        pass

    # Επιστρέφει αριθμό αν υπάρχει κενό στο κέντρο η σε μια γωνία ή None αν όχι
    def center_or_corners(self):
        pass

    # Επιστρέφει μια τυχαία θέση από τις θέσεις του πίνακα που είναι κενή
    def random_place(self, table=[1, 3, 7, 9]):
        pass

    # Επιστρέεφει list με τους αριθμούς που δεν παίχθηκαν
    def toplay(self):
        to_play = []
        for i in range(9):
            if i not in self.played():
                to_play.append(i)
        return to_play


class GameControler():

    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.tablo = None
        self.score_board = None
        self.count = 0
        self.game_count = 0

    def get_settings(self, player1_entry, player2_entry, cd1, cd2, selected_level):
        if cd1 == 0:
            self.player1 = Player(player1_entry)
        else:
            if selected_level == "Easy":
                self.player1 = EasyComPlayer(player1_entry)
            else:
                self.player1 = NormalComPlayer(player1_entry)
        if cd2 == 0:
            self.player2 = Player(player2_entry)
        else:
            if selected_level == "Easy":
                self.player2 = EasyComPlayer(player2_entry)
            else:
                self.player2 = NormalComPlayer(player2_entry)
        self.tablo = Table(self.player1, self.player2)
        self.score_board = ScoreBoard(self.player1, self.player2)

    def current_player(self):
        if len(self.tablo.played()) == 0:
            if self.game_count % 2 == 0:
                return self.player1
            else:
                return self.player2

        if self.count % 2 == 0:

            return self.player1
        else:
            return self.player2

    def other_player(self):
        if self.current_player() == self.player1:
            return self.player2
        else:
            return self.player1

    def new_game(self):
        self.game_count += 1
        self.count = self.game_count % 2
        self.tablo.tablo[self.player1] = []
        self.tablo.tablo[self.player2] = []

    def check_for_winner(self):
        winning_series = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7]]
        for j in winning_series:
            if all(i in self.tablo.tablo[self.current_player()] for i in j):
                return True
        else:
            return False

    def check_for_draw(self):
        if len(self.tablo.played()) == 9:
            return True
        else:
            return False

    def check(self, number, label):
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
                return "destroy"
            self.count += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("450x150")
        self.title('Tik Tok Toe')

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.create_widgets()

    def create_widgets(self):
        # player1
        player1_label = ttk.Label(self, text="Player1:")
        player1_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.player1_entry = ttk.Entry(self)
        self.player1_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # player1 = computer
        self.cd1 = tk.IntVar()
        self.p1_iscom = ttk.Checkbutton(self, text='isComputer', variable=self.cd1)
        self.p1_iscom.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

        # player2
        player2_label = ttk.Label(self, text="Player2:")
        player2_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.player2_entry = ttk.Entry(self)
        self.player2_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # player2 = computer
        self.cd2 = tk.IntVar()
        self.p2_iscom = ttk.Checkbutton(self, text='isComputer', variable=self.cd2)
        self.p2_iscom.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

        # Computer Intelligence
        intell_label = ttk.Label(self, text='Computer Inteligence:  ')
        intell_label.grid(column=0, row=3, columnspan=2, sticky=tk.SE, padx=5, pady=5)

        self.selected_level = tk.StringVar()
        level = ('Easy', 'Normal')
        self.intell_choise = ttk.Combobox(self, textvariable=self.selected_level, values=level, state='readonly')
        self.intell_choise.bind('<<ComboboxSelected>>', self.level_changed)
        self.intell_choise.grid(column=2, row=3, sticky=tk.W)

        # submit button
        submit_button = ttk.Button(self, command=self.button_push, text="Submit")
        submit_button.grid(column=2, row=4, sticky=tk.S, padx=5, pady=5)

    def level_changed(self, event):
        pass

    def button_push(self):
        global gc
        gc = GameControler()
        gc.get_settings(self.player1_entry.get(), self.player2_entry.get(), self.cd1.get(), self.cd2.get(),
                        self.selected_level.get())
        App.destroy(self)
        Game()


class Winner(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("270x270")
        self.title('TikTakToe')
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        if gc.check_for_draw():
            self.label_winner = tk.Label(self, borderwidth=2, relief="groove", text="The Game is DRAW",
                                         font=("Arial", 12), width=30)
        else:
            self.label_winner = tk.Label(self, borderwidth=2, relief="groove", text="The winner is:",
                                         font=("Arial", 12), width=30)
            self.label_winner_name = tk.Label(self, borderwidth=2, relief="groove",
                                              text=f"{gc.current_player().name}", font=("Arial", 12), width=12)
            self.label_winner_name.grid(column=0, columnspan=4, row=1)
        self.label_winner.grid(column=0, columnspan=4, row=0)
        self.label_score = tk.Label(self, borderwidth=2, relief="groove",
                                    text="The Score is", font=("Arial", 12), width=12)
        self.label_score.grid(column=0, columnspan=4, row=2, pady=(5, 0))
        self.label_p1 = tk.Label(self, borderwidth=2, relief="groove",
                                 text=f"{gc.player1.name}", font=("Arial", 12), width=12)
        self.label_p1.grid(column=0, columnspan=2, row=3)
        self.label_p2 = tk.Label(self, borderwidth=2, relief="groove",
                                 text=f"{gc.player2.name}", font=("Arial", 12), width=12)
        self.label_p2.grid(column=2, columnspan=2, row=3)
        self.label_score_p1 = tk.Label(self, borderwidth=2, relief="groove",
                                       text=f"{gc.score_board.board[gc.player1]}",
                                       font=("Arial", 12), width=12)
        self.label_score_p1.grid(column=0, columnspan=2, row=4)
        self.label_score_p2 = tk.Label(self, borderwidth=2, relief="groove",
                                       text=f"{gc.score_board.board[gc.player2]}",
                                       font=("Arial", 12), width=12)
        self.label_score_p2.grid(column=2, columnspan=2, row=4)
        self.button_continue = ttk.Button(self, command=self.button1_push, text="Continue")
        self.button_continue.grid(column=0, row=5, sticky=tk.E, padx=1, pady=1)
        self.button_end = ttk.Button(self, command=self.button2_push, text="End")
        self.button_end.grid(column=3, row=5, sticky=tk.W, padx=1, pady=1)

    def button1_push(self):
        gc.new_game()
        Winner.destroy(self)
        Game()

    def button2_push(self):
        Winner.destroy(self)


class Game(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title('TikTakToe')
        self.resizable(0, 0)
        self.create_widgets()
        gc.current_player().play()

    def create_widgets(self):
        self.label1 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label1.grid(column=0, row=0, padx=(110, 0), sticky=tk.W)
        self.label1.bind("<Button-1>", self.label1_click)
        self.label2 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label2.grid(column=1, row=0, sticky=tk.W)
        self.label2.bind("<Button-1>", self.label2_click)
        self.label3 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label3.grid(column=2, row=0, sticky=tk.W)
        self.label3.bind("<Button-1>", self.label3_click)
        self.label4 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label4.grid(column=0, padx=(110, 0), row=1, sticky=tk.W)
        self.label4.bind("<Button-1>", self.label4_click)
        self.label5 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label5.grid(column=1, row=1, sticky=tk.W)
        self.label5.bind("<Button-1>", self.label5_click)
        self.label6 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label6.grid(column=2, row=1, sticky=tk.W)
        self.label6.bind("<Button-1>", self.label6_click)
        self.label7 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label7.grid(column=0, padx=(110, 0), row=2, sticky=tk.W)
        self.label7.bind("<Button-1>", self.label7_click)
        self.label8 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label8.grid(column=1, row=2, sticky=tk.W)
        self.label8.bind("<Button-1>", self.label8_click)
        self.label9 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label9.grid(column=2, row=2, sticky=tk.W)
        self.label9.bind("<Button-1>", self.label9_click)
        self.label_now_plays = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 12), width=25)
        self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))
        self.label_now_plays.grid(column=0, columnspan=4, row=3, padx=(40, 0), sticky=tk.S)
        self.score_board_label = tk.Label(self, borderwidth=2, relief="groove", anchor="center", text="Πίνακας Score",
                                          font=("Arial", 15), width=16)
        self.score_board_label.grid(column=0, columnspan=3, row=6, sticky=tk.NSEW, padx=(80, 0), pady=(10, 0))
        self.score_board_p1 = tk.Label(self, borderwidth=2, relief="groove", text=f"{gc.player1.name}",
                                       font=("Arial", 10), width=15)
        self.score_board_p1.grid(column=0, columnspan=2, row=7)
        self.score_board_p2 = tk.Label(self, borderwidth=2, relief="groove", text=f"{gc.player2.name}",
                                       font=("Arial", 10), width=15)
        self.score_board_p2.grid(column=2, columnspan=2, row=7)
        self.score_board_p1score = tk.Label(self, borderwidth=2, relief="groove",
                                            text=f"{gc.score_board.board[gc.player1]}",
                                            font=("Arial", 15), width=11)
        self.score_board_p1score.grid(column=0, columnspan=2, row=8)
        self.score_board_p2score = tk.Label(self, borderwidth=2, relief="groove",
                                            text=f"{gc.score_board.board[gc.player2]}",
                                            font=("Arial", 15), width=11)
        self.score_board_p2score.grid(column=2, columnspan=2, row=8)

    def label1_click(self, event):
        if gc.check(1, self.label1) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label2_click(self, event):
        if gc.check(2, self.label2) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label3_click(self, event):
        if gc.check(3, self.label3) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label4_click(self, event):
        if gc.check(4, self.label4) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label5_click(self, event):
        if gc.check(5, self.label5) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label6_click(self, event):
        if gc.check(6, self.label6) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label7_click(self, event):
        if gc.check(7, self.label7) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label8_click(self, event):
        if gc.check(8, self.label8) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))

    def label9_click(self, event):
        if gc.check(9, self.label9) == "destroy":
            Game.destroy(self)
            Winner()
        else:
            self.label_now_plays.config(text="Current Player: {}".format(gc.current_player().name))


if __name__ == "__main__":
    app = App()
    app.mainloop()
