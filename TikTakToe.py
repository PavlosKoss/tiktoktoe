import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
from threading import *
import time


# Class human player
class Player:
    """
    Παίχτης - Άνθρωπος

    Πεδία
    ----------
    name : str
    Όνομα παίχτη

    Μέθοδοι
    ----------
    play
    επιστρέφει 0
    """

    def __init__(self, name):
        self.name = name

    def play(self, table):
        return 0


# Class Computer Easy player
class EasyComPlayer(Player):
    """
       Παίχτης - Υπολογιστής easy

       Πεδία
       ----------
       name : str
       Όνομα παίχτη

       Μέθοδοι
       ----------
       play(table, other_player)
       επιστρέφει μια τυχαία θέση που δεν έχει παιχτεί
       """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table):
        # Παίρνει έναν τυχαίο αριθμό που δεν έχει παιχτεί (table.rantom_place)
        # και επιστρέφει μια θέση
        return table.random_place()


class NormalComPlayer(Player):
    """
       Παίχτης - Υπολογιστής Normal

       Πεδία
       ----------
       name : str
       Όνομα παίχτη

       Μέθοδοι
       ----------
       play(table)
       Ελέγχει αν ο παίχτης μπορεί να νικήσει με μια κίνηση και επιστρέφει τη θέση
       Ελέγχει αν ο αντίπαλος μπορεί να νικήσει με μια κίνηση και επιστρέφει τη θέση
       Αν η κεντρική θέση είναι ελεύθερη την επιστρέφει
       Ελέγχει αν υπάρχει γωνιακή θέση και επιστρέφει μια τυχαία γωνιακή θέση
       Αν δεν ισχύει τίποτα απο τα παραπάνω επιστρέφει μια τυχαία θέση

       """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table):

        if table.ready_to_win(self) is not None:
            return table.ready_to_win(self)
        if table.ready_to_win(gc.other_player()) is not None:
            return table.ready_to_win(gc.other_player())
        if table.place_in_center() is not None:
            return 5
        if table.place_in_corner() is not None:
            return table.place_in_corner()
        else:
            return table.random_place()


class ScoreBoard:
    """
        Πίνακας Σκορ
        κρατάει το σκορ των νικών των παιχτών και αυξάνει το σκορ του νικητή

        Πεδία
        ----------
        player1 : Player()
        player2 : Player()
        board : dict
            Λεξικό με κλειδί τον παίχτη και δεδομένα το σκορ


        Μέθοδοι
        ----------
        winner(player)
        Αυξάνει κατά 1 το σκορ του νικητή

        """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = {player1: 0, player2: 0}

    def winner(self, player):
        self.board[player] += 1


class Table:
    """
            κρατά και διαχειρίζετε τον πίνακα των θέσεων που έχουν παιχτεί ανα παίκτη.


            Πεδία
            ----------
            player1 : Player()
            player2 : Player()
            tablo : dict
                Λεξικό με κλειδί τον παίχτη και δεδομένα τις θέσεις που έχει παίξει
            winning_series : list
                Πίνακας με τους νικητήριους συνδιασμούς θέσεων

            Μέθοδοι
            ----------
            place_move(player, number)
                τοποθετεί την κίνηση του παίχτη στο λεξικό

            played()
                επιστρέφει πίνακα με τις θέσεις που έχουν παιχτεί

            toplay()
                επιστρέφει πίνακα με τις θέσεις που δεν έχουν παιχτεί

            ready_to_win(player)
                Αν υπάρχει μια θέση που συμπληρώνει νικητήρια στήλη για τον παίχτη
                την επιστρέφει αλλιώς επιστρέφει None

            place_in_center()
                Αν είναι κενή η κεντρική θέση την επιστρέφει αλλιώς επιστρέφει None

            place_in_corner()
                Αν υπάρχουν κενές γωνιακές θέσεις επιστρέφει μια τυχαία αλλιώς επιστρέφει None

            random_place(self)
                Επιστρέφει μια τυχαία θέση

            """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.tablo = {self.player1: [], self.player2: []}
        self.winning_series = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def place_move(self, player, number):
        self.tablo[player].append(number)

    def played(self):
        return self.tablo[self.player1] + self.tablo[self.player2]

    def toplay(self):
        to_play = []
        for i in range(1, 10):
            if i not in self.played():
                to_play.append(i)
        return to_play

    def ready_to_win(self, player):
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
        if 5 not in self.played():
            return 5
        else:
            return None

    def place_in_corner(self):
        if all(number in self.played() for number in [1, 3, 7, 9]):
            return None
        else:
            while True:
                number = random.choice([1, 3, 7, 9])
                if number not in self.played():
                    return number

    def random_place(self):
        return random.choice(self.toplay())


class GameControler:
    """
        Διαχειριστής παιχνιδιού


        Πεδία
        ----------
        player1 : Player()
        player2 : Player()
        tablo : Table()
        score_board : ScoreBoard()
        game : Game()
        count : int
            Μετρητής κινήσεων στην παρτίδα
        game_count : int
            Μετριτής παρτίδων
        couples : int
            1 για human - human, 2 for human - computer, 3 for computer - computer


        Μέθοδοι
        ----------
        get_settings(player1_entry, player2_entry, cd1, cd2, selected_level)
            Ελέγχει το είδος των παιχτών και δημιουργεί τα αντικείμενα Player1 & Player2
            Δημιουργεί τα αντικείμενα tablo & score_board

        game_by_couple()
            Ελέγχει το ζευγάρι των παιχτών και ορίζει την couples.
            Έπειτα δημιουργεί ένα αντικείμενο Game() και το εκτελεί

        current_player()
            ελέγχει τον counter και αν  είναι ζηγός ο παίχτης είναι ο player1 αλλιώς ο player2

        other_player()
            επιστρέφει τον παίχτη που δεν παίζει αυτή τη στιγμή

        new_game()
            αλλάζει τους counters και αδειάζει το tablo αν ο game_count δεν διαιρήτε με το μηδέν
            δίνει στον count την 1 για να παίξει πρότος ο δευτερος παίχτης

        check_for_winner()
            ελέγχει αν ο παίχτης που παίζει τώρα έχει συμπληρώσει κάποια νικητήρια στήλη και επιστρέφει
            True ή False

        check_for_draw()
            ελέγχει αν έχουν παιχτεί όλες οι θέσεις και αν ναι επιστρέφει True αλλιώς False

        click_for_computer()
            προσπαθεί να παίξει για τον υπολογιστή αν ο παίχτης είναι human
            επιστρέφει None οπότε αποτυγχάνει και δεν κάνει κάτι

        check(number, label)
            ελέγχει αν το επιλεγμένο κελί έχει παιχτεί οπότε και εμφανίζει μήνυμα.
            αν όχι ελέγχει ποιός παίχτης έπαιξε καλεί την tablo.place_move για να τοποθετήσει την κίνηση στο tablo,
            δίνει το αντίστοιχο text στο label (Χ ή Ο) και αυξάνει τον count
            τέλος ελέγχει αν υπάρχει νικητής ή ισοπαλία και αν ναι επιστρέφει destroy

        color_the_winning_line()
            βρήσκει ποιά είναι η νικηρήρια σειρά και χρωματίζει κόκκινα τα γράμματα στα labels

        """

    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.tablo = None
        self.score_board = None
        self.game = None
        self.count = 0
        self.game_count = 0
        self.couples = 0

    def get_settings(self, player1_entry, player2_entry, cd1, cd2, selected_level1, selected_level2):
        if cd1 == 0:
            self.player1 = Player(player1_entry)
        else:
            if selected_level1 == "Easy":
                self.player1 = EasyComPlayer(player1_entry + "(ECom1)")
            else:
                self.player1 = NormalComPlayer(player1_entry + "(NCom1)")
        if cd2 == 0:
            self.player2 = Player(player2_entry)
        else:
            if selected_level2 == "Easy":
                self.player2 = EasyComPlayer(player2_entry + "(ECom2)")
            else:
                self.player2 = NormalComPlayer(player2_entry + "(NCom2)")
        self.tablo = Table(self.player1, self.player2)
        self.score_board = ScoreBoard(self.player1, self.player2)

    def game_by_couple(self):
        if self.player1.play(self.tablo) == 0 and self.player2.play(self.tablo) == 0:
            self.couples = 1
        if self.player1.play(self.tablo) != 0 and self.player2.play(self.tablo) != 0:
            self.couples = 3
        else:
            self.couples = 2
        self.game = Game()
        self.game.mainloop()

    def current_player(self):
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
        for j in self.tablo.winning_series:
            if all(i in self.tablo.tablo[self.current_player()] for i in j):
                return True
        else:
            return False

    def check_for_draw(self):
        if len(self.tablo.played()) == 9:
            return True
        else:
            return False

    def click_for_computer(self):
        try:
            eval('self.game.label{}_click("<Button-1>")'.format(
                self.current_player().play(self.tablo)))
        except:
            pass

    def check(self, number, label, game):
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
                return "destroy"
            self.count += 1
            game.label_now_plays.config(text="Now Plays: {}".format(self.current_player().name))
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to choose an empty place')

    def color_the_winning_line(self):
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
        Θυγατρική κλάση της Thread για την εκτέλεση κώδικα σε ξεχωριστό tread ωστε να ανανεώνεται
        το παράθυρο του παιχνιδιού όταν και οι δύο παίχτες είναι ο υπολογιστής.

        Πεδία
        ----------
        gc : GameControler()
        game : Game()


        Μέθοδοι
        ----------
        run()
        αντικαθιστά την run του parent με τον κώδικα που θέλουμε να εκτελέσουμε στο thread
        με καθυστερηση 1 sec τοποθετεί τις κινήσεις του κάθε παίχτη μέχρι να έχουμε νικητή ή ισσοπαλία


        """

    def __init__(self, game):
        super().__init__()
        self.game = game

    def run(self):
        while True:
            time.sleep(1)
            number = gc.current_player().play(gc.tablo)
            # Μέσα στην if εκτελείται η check και μετά επιστρέφει
            if gc.check(number, eval(f"self.game.label{number}"), self.game) == "destroy":
                break


class App(tk.Tk):
    """
        Αρχικό παράθυρο συλογής πληροφοριών

        Πεδία
        ----------

        Μέθοδοι
        ----------
        create_widgets()
        δημιουργεί τα στοιχεία του παραθύρου:
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

        button_push()
        συμβάν κατά το πάτημα του submit_button
        δημιουργεί ένα global αντικείμενο GameControler και στη συμέχεια καλή την get_settings μέθοδο
        αυτού όπου και τοποθετεί τα πεδία που συμπληρώσαμε. στη συνέχεια καταστρέφει τον εαυτό της
        και καλεί την game_by_couple() του διαχειριστή του παιχνιδιού.

    """

    def __init__(self):
        super().__init__()
        self.geometry("450x150")
        self.title('Tik Tok Toe')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=1)
        self.create_widgets()

    # στοιχεία παραθύρου
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
        self.selected_level1 = tk.StringVar()
        self.selected_level2 = tk.StringVar()
        level = ('Easy', 'Normal')
        self.intell_choise1 = ttk.Combobox(self, textvariable=self.selected_level1, values=level, state='readonly')
        self.intell_choise1.current(0)
        self.intell_choise1.grid(column=3, row=0, sticky=tk.W)
        self.intell_choise2 = ttk.Combobox(self, textvariable=self.selected_level2, values=level, state='readonly')
        self.intell_choise2.current(0)
        self.intell_choise2.grid(column=3, row=1, sticky=tk.W)

        # Submit Button
        submit_button = ttk.Button(self, command=self.button_push, text="Submit")
        submit_button.grid(column=2, row=4, sticky=tk.S, padx=5, pady=5)

    def button_push(self):
        global gc
        gc = GameControler()
        gc.get_settings(self.player1_entry.get(), self.player2_entry.get(), self.cd1.get(), self.cd2.get(),
                        self.selected_level1.get(), self.selected_level2.get())
        App.destroy(self)
        gc.game_by_couple()


class Game(tk.Tk):
    """
        Παράθυρο παιχνιδιού
        κατά την αρχικοποίηση ελέγχει αν παίζουν δύο υπολογιστές και αν ναι δημιουργεί ένα αντικείμενο
        PlayTwoComputers και καλεί την μέθοδο του run(), στη συνέχεια καλεί την open_winner με καθυστέρηση
        10 δευτερολέπτων για να προλάβουν να γίνουν οι κινήσεις των παικτών.
        Αν δεν παίζουν 2 υπολογιστές ελέγχει αν παίζει human και αν όχι εκτελεί την κίνηση του υπολογιστή




        Πεδία
        ----------

        Μέθοδοι
        ----------

        create_widgets()
        δημιουργεί τα στοιχεία του παραθύρου:
        label1, label2, label3, label4, label5, label6, label7, label8, label9 : ttk.Label τα οποία η μέθοδος bind
        ενεργοποιήτε μόνο αν τουλάχιστον ένας παίκτης είναι human
        label_now_plays : ttk.Label
        score_board_label : tk.Label
        score_board_p1 : tk.Label
        score_board_p2 : tk.Label
        score_board_p1score : tk.Label
        score_board_p2score : tk.Label

        open_winner()
        καλεί το TopLevel Winner

        label1_click(event)
        καλεί την check την εκτελεί με παράμετρο τον αριθμό του κελιού και αν επιστρέψει "destroy" καλεί
        την open_winner() με καθυστέρηση αλλιώς καλεί την click_for_computer η οποία αν είναι
        ο παίκτης human δεν κάνει τίποτα και περημένει από τον
        παίκτη να κάνει κάποια κίνηση.

        το ίδιο για κάθε labelx_click()

       """

    def __init__(self):
        super().__init__()
        self.geometry("250x400+50+50")
        self.title('TikTakToe')
        self.resizable(False, False)
        self.create_widgets()
        if gc.couples == 3:
            play = PlayTwoComputers(self)
            play.start()
            self.after(10000, self.open_winner)

        elif gc.current_player().play(gc.tablo) != 0:
            eval('self.label{}_click("<Button-1>")'.format(gc.current_player().play(gc.tablo)))

    def create_widgets(self):
        self.camvas = tk.Canvas(self, width=220, height=220)
        self.camvas.create_line(68, 0, 68, 215, width=4, fill="grey")
        self.camvas.create_line(136, 0, 136, 215, width=4, fill="grey")
        self.camvas.create_line(0, 72, 210, 72, width=4, fill="grey")
        self.camvas.create_line(0, 142, 210, 142, width=4, fill="grey")
        self.camvas.grid(column=0, columnspan=2, row=0)
        self.label1 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label1.place(x=18, y=6)
        if gc.couples != 3 and gc.check_for_winner() is False and gc.check_for_draw() is False:
            self.label1.bind("<Button-1>", self.label1_click)
        self.label2 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label2.place(x=85, y=6)
        if gc.couples != 3:
            self.label2.bind("<Button-1>", self.label2_click)
        self.label3 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label3.place(x=157, y=6)
        if gc.couples != 3:
            self.label3.bind("<Button-1>", self.label3_click)
        self.label4 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label4.place(x=18, y=76)
        if gc.couples != 3:
            self.label4.bind("<Button-1>", self.label4_click)
        self.label5 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label5.place(x=85, y=76)
        if gc.couples != 3:
            self.label5.bind("<Button-1>", self.label5_click)
        self.label6 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label6.place(x=157, y=76)
        if gc.couples != 3:
            self.label6.bind("<Button-1>", self.label6_click)
        self.label7 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label7.place(x=18, y=146)
        if gc.couples != 3:
            self.label7.bind("<Button-1>", self.label7_click)
        self.label8 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label8.place(x=85, y=146)
        if gc.couples != 3:
            self.label8.bind("<Button-1>", self.label8_click)
        self.label9 = ttk.Label(self, text="", font=("Arial", 40), width=2)
        self.label9.place(x=157, y=146)
        if gc.couples != 3:
            self.label9.bind("<Button-1>", self.label9_click)
        self.label_now_plays = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 12), width=25)
        self.label_now_plays.config(text="Now Plays: {}".format(gc.current_player().name))
        self.label_now_plays.grid(column=0, columnspan=2, row=1, padx=(0, 0), sticky=tk.S)
        self.score_board_label = tk.Label(self, borderwidth=2, relief="groove", anchor="center", text="Πίνακας Score",
                                          font=("Arial", 15), width=16)
        self.score_board_label.grid(column=0, columnspan=2, row=6, sticky=tk.NSEW, padx=(0, 0), pady=(10, 0))
        self.score_board_p1 = tk.Label(self, borderwidth=2, relief="groove", text=f"{gc.player1.name}",
                                       font=("Arial", 10), width=15)
        self.score_board_p1.grid(column=0, row=7, sticky=tk.NSEW, padx=(0, 0))
        self.score_board_p2 = tk.Label(self, borderwidth=2, relief="groove", text=f"{gc.player2.name}",
                                       font=("Arial", 10), width=15)
        self.score_board_p2.grid(column=1, row=7, sticky=tk.NSEW, padx=(0, 0))
        self.score_board_p1score = tk.Label(self, borderwidth=2, relief="groove",
                                            text=f"{gc.score_board.board[gc.player1]}",
                                            font=("Arial", 15), width=11)
        self.score_board_p1score.grid(column=0, row=8)
        self.score_board_p2score = tk.Label(self, borderwidth=2, relief="groove",
                                            text=f"{gc.score_board.board[gc.player2]}",
                                            font=("Arial", 15), width=11)
        self.score_board_p2score.grid(column=1, row=8)

    def open_winner(self):
        Winner()

    def label1_click(self, event):
        if gc.check(1, self.label1, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label2_click(self, event):
        if gc.check(2, self.label2, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label3_click(self, event):
        if gc.check(3, self.label3, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label4_click(self, event):
        if gc.check(4, self.label4, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label5_click(self, event):
        if gc.check(5, self.label5, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label6_click(self, event):
        if gc.check(6, self.label6, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label7_click(self, event):
        if gc.check(7, self.label7, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label8_click(self, event):
        if gc.check(8, self.label8, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()

    def label9_click(self, event):
        if gc.check(9, self.label9, self) == "destroy":
            self.after(1000, self.open_winner)
        else:
            gc.click_for_computer()


class Winner(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.geometry("350x200+250+250")
        self.title('TikTakToe')
        self.grab_set()
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        if gc.check_for_winner():

            self.label_winner = tk.Label(self, text="The winner is:",
                                         font=("Arial", 12))
            self.label_winner.grid(column=0, row=0)
            self.label_winner_name = tk.Label(self,text=f"{gc.current_player().name}", font=("Arial", 14), width=24)
            self.label_winner_name.grid(column=0, columnspan=2, row=1)
        else:
            self.label_winner = tk.Label(self, text="The Game is DRAW", font=("Arial", 12), width=30)
        self.label_winner.grid(column=0, columnspan=2, row=0)
        self.label_score = tk.Label(self, text="The Score is", font=("Arial", 12), width=12)
        self.label_score.grid(column=0, columnspan=2, row=2, pady=(5, 0))
        self.label_p1 = tk.Label(self, text=f"{gc.player1.name}", font=("Arial", 9), width=24)
        self.label_p1.grid(column=0, row=3)
        self.label_p2 = tk.Label(self,text=f"{gc.player2.name}", font=("Arial", 9), width=24)
        self.label_p2.grid(column=1, row=3)
        self.label_score_p1 = tk.Label(self, text=f"{gc.score_board.board[gc.player1]}", font=("Arial", 12), width=12)
        self.label_score_p1.grid(column=0, row=4)
        self.label_score_p2 = tk.Label(self, text=f"{gc.score_board.board[gc.player2]}", font=("Arial", 12), width=12)
        self.label_score_p2.grid(column=1, row=4)
        self.button_continue = ttk.Button(self, command=self.button1_push, text="Continue")
        self.button_continue.grid(column=0, row=5, padx=1, pady=20)
        self.button_end = ttk.Button(self, command=self.button2_push, text="End")
        self.button_end.grid(column=1, row=5, padx=1, pady=20)

    def button1_push(self):
        gc.new_game()
        self.grab_release()
        gc.game.destroy()
        gc.game_by_couple()

    def button2_push(self):
        gc.game.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
