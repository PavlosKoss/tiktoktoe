import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
from threading import *
import time


class Player:
    """
    Παίχτης - Άνθρωπος

    Πεδία
    ----------
    name : str
        Όνομα παίχτη

    Μέθοδοι
    ----------
    play()
        επιστρέφει 0
    """

    def __init__(self, name):
        self.name = name

    def play(self, table):
        return 0


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
            Που θα παίξει ο παίκτης
       """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table):
        """
        Επιστρέφει μια τυχαία θέση που δεν έχει παιχτεί.

        Παράμετροι
        ----------
        table: Table()
             Το αντικείμενο που διαχειρίζεται το ταμπλό

        Επιστρέφει
        ---------
        int:int
            Η θέση που θα παίξει ο παίκτης
        """
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
           Που θα παίξει ο παίκτης
       """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table):
        """
        Ελέγχει αν ο παίχτης μπορεί να νικήσει με μια κίνηση και επιστρέφει τη θέση
        Ελέγχει αν ο αντίπαλος μπορεί να νικήσει με μια κίνηση και επιστρέφει τη θέση
        Αν η κεντρική θέση είναι ελεύθερη την επιστρέφει
        Ελέγχει αν υπάρχει γωνιακή θέση και επιστρέφει μια τυχαία γωνιακή θέση
        Αν δεν ισχύει τίποτα απο τα παραπάνω επιστρέφει μια τυχαία θέση
        Παράμετροι
        ----------
        table: Table()
             Το αντικείμενο που διαχειρίζεται το ταμπλό
        Επιστρέφει
        ---------
        int:int
            Η θέση που θα παίξει ο παίκτης
        """

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


class HardComPlayer(Player):
    """
    Παίχτης - Υπολογιστής Good

    Πεδία
    ----------
    name : str
        Όνομα παίχτη

    Μέθοδοι
    ----------
    play(table)
        Που θα παίξει ο παίκτης
    """

    def __init__(self, name):
        super().__init__(name)

    def play(self, table):
        """
        Ελέγχει αν ο παίχτης μπορεί να νικήσει με μια κίνηση και επιστρέφει τη θέση
        Ελέγχει αν ο αντίπαλος μπορεί να νικήσει με μια κίνηση και επιστρέφει τη θέση
        Ελέγχει αν παίζει πρώτος και αν ναι επιστρέφει μια τυχαία γωνία
        Αν έχουν παιχτεί οι τρείς θέσεις σε μια διαγώνιο ελέγχει αν η θέση 5 είναι
        καταλυμένη από τον εαυτό του και αν ναι επιστρέφει μια μεσαία θέση
        Αν ο αντίπαλος στην τρίτη κίνηση έχει δυο θέσεις στα gammas τότε παίζει μια θέση από τις υπόλοιπες
        Αν η κεντρική θέση είναι ελεύθερη την επιστρέφει
        Ελέγχει αν υπάρχει γωνιακή θέση και επιστρέφει μια τυχαία γωνιακή θέση
        Αν δεν ισχύει τίποτα απο τα παραπάνω επιστρέφει μια τυχαία θέση

        Παράμετροι
        ----------
        table:Table()
            Το αντικείμενο που διαχειρίζεται το ταμπλό
        Επιστρέφει
        ---------
        int:int
            Η θέση που θα παίξει ο παίκτης
        """
        diag = ((1, 5, 9), (3, 5, 7))
        gammas = (
            (1, 2, 3, 6), (2, 3, 6, 9), (3, 6, 9, 8), (6, 9, 8, 7), (9, 8, 7, 4), (8, 7, 4, 1), (7, 4, 1, 2),
            (4, 1, 2, 3))
        if table.ready_to_win(self) is not None:
            return table.ready_to_win(self)
        if table.ready_to_win(gc.other_player()) is not None:
            return table.ready_to_win(gc.other_player())
        if len(table.played()) == 0:
            return random.choice([1, 3, 7, 9])
        if len(table.played()) == 3:
            for diagonios in diag:
                if all(j in table.played() for j in diagonios):
                    if 5 in table.tablo[self]:
                        return random.choice([2, 4, 6, 8])
            for gamma in gammas:
                if len(set(gamma).intersection(table.tablo[gc.other_player()])) == 2:
                    return random.choice(list(set(gamma).difference(table.tablo[gc.other_player()])))
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
        1ος παίκτης
    player2 : Player()
        2ος παίκτης
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
        """
        Προσθέτει τη νίκη στο σκορ του παίκτη

        Παράμετροι
        ----------
        player:Player()
            Ο παίκτης που νίκησε

        Επιστρέφει
        ----------

        """
        self.board[player] += 1


class Table:
    """
    κρατά και διαχειρίζετε τον πίνακα των θέσεων που έχουν παιχτεί ανα παίκτη.

    Πεδία
    ----------
    player1 : Player()
        1ος παίκτης
    player2 : Player()
        2ος παίκτης
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
        """
        τοποθετεί την κίνηση του παίκτη στο tablo

        Παράμετροι
        ----------
        player: Player()
            Ο παίκτης που έκανε την κίνηση
        number: int
            Η θέση που έπαιξε ο παίκτης

        Επιστρέφει
        ----------

        """
        self.tablo[player].append(number)

    def played(self):
        """
        επιστρέφει μια λίστα με της θέσεις που έχουν παιχτεί

        Παράμετροι
        ----------
        number: int (1 to 9)
            αριθμός που δηλώνει τη θέση που έπαιξε ο παίχτης
        label: Game.label'n'
            το label στο οποίο έγινε η κίνηση
        game: Game()

        Επιστρέφει
        ----------
        list
            Λίστα με τις θέσεις που έχουν παιχτεί
        """
        return self.tablo[self.player1] + self.tablo[self.player2]

    def toplay(self):
        """
        Επιστρέφει μια λίστα με της ελεύθερες θέσεις του tablo

        Παράμετροι
        ----------

        Επιστρέφει
        ----------
        to_play: list
            Λίστα με τις ελεύθερες θέσεις του tablo
        """
        to_play = []
        for i in range(1, 10):
            if i not in self.played():
                to_play.append(i)
        return to_play

    def ready_to_win(self, player):
        """
        ελέγχει αν ο διθέντας παίκτης έχει κάποια κίνηση για να νικήσει

        Παράμετροι
        ----------
        player: Player()

        Επιστρέφει
        ----------
        None
            αν δεν υπάρχει κάποια κίνηση νίκης
        number1 : int
            την θέση που πρέπει να παίξει ο παίκτης για να νικήσει
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
        ελέγχει αν η μεσαία θέση είναι ελεύθερη και την επιστρέφει αν ναι, αλλιως επιστρέφει None

        Παράμετροι
        ----------

        Επιστρέφει
        None αν η μεσαία θέση είναι καταλυμένη
        5 : int
            αν η μεσαία θέση δεν είναι καταλυμένη.
        ----------

        """
        if 5 not in self.played():
            return 5
        else:
            return None

    def place_in_corner(self):
        """
        ελέγχει αν έχουν παιχτεί όλες οι γωνιακές θέσεις και επιστρέφει None αν ναι μια τυχαία
          γωνιακή θέση αν όχι.

        Παράμετροι
        ----------

        Επιστρέφει
        ----------
        None αν δεν υπάρχει κενή γωνιακή θέση, αλλιώς μια τυχαία γωνιακή θέση που δεν έχει παιχτεί
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
        Επιστρέφει μια τυχαία θέση που δεν έχει παιχτεί

        Παράμετροι
        ----------

        Επιστρέφει
        ----------
        Μια τυχαία θέση που δεν έχει παιχτεί
        """
        return random.choice(self.toplay())


class GameController:
    """
    Διαχειριστής παιχνιδιού

    Πεδία
    ----------
    player1 : Player()
        Παίκτης Χ
    player2 : Player()
        Παίκτης Ο
    tablo : Table()
        αντικείμενο τύπου Table
    score_board : ScoreBoard()
        αντικείμενο τύπου ScoreBoard
    game : Game()
        αντικείμενο τύπου Game

    count : int
        Μετρητής κινήσεων στην παρτίδα
    game_count : int
        Μετρητής παρτίδων
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
        αν όχι ελέγχει ποιος παίχτης έπαιξε καλεί την tablo.place_move για να τοποθετήσει την κίνηση στο tablo,
        δίνει το αντίστοιχο text στο label (Χ ή Ο) και αυξάνει τον count
        τέλος ελέγχει αν υπάρχει νικητής ή ισοπαλία και αν ναι επιστρέφει destroy
    color_the_winning_line()
        βρίσκει ποια είναι η νικητήρια σειρά και χρωματίζει κόκκινα τα γράμματα στα labels
    """

    def __init__(self):
        """
        Αρχικοποιεί τα πεδία της GameController

        Παράμετροι
        ----------
        player1 : Player
            δημιουργία αντικειμένου παίκτη για τον 1ο παίκτη
        player2 : Player
            δημιουργία αντικειμένου παίκτη για τον 2ο παίκτη
        score_board : ScoreBoard
            δημιουργία αντικειμένου score board
        game : Game
            δημιουργία αντικειμένου Game
        count : int
            μεταβλητή που μετράει τις κινήσεις των παιχτών
        game_count : int
            μεταβλητή που μετράει τον αριθμό των παιχνιδιών
        couples : int
            μεταβλητή που χαρατηρίζει το ζευγάρι των παιχτών:
                1 = human vs humman
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

    def get_settings(self, player1_entry, player2_entry, cd1, cd2, selected_level1, selected_level2):
        """
        Ελέγχει το είδος των παιχτών και δημιουργεί τα αντικείμενα Player1 & Player2
        Δημιουργεί τα αντικείμενα tablo & score_board

        Παράμετροι
        __________
        player1_entry: str
            Όνομα του 1ου παίκτη
        player2_entry: str
            Όνομα του 2ου παίκτη
        cd1: int (0 or 1)
            0 για human 1 για Computer για τον 1ο παίκτη
        cd2: int (0 or 1)
            0 για human 1 για Computer για τον 2ο παίκτη
        selected_level1: str
            Easy - Normal - Hard για τον 1ο computer παίκτη
        selected_level2: str
            Easy - Normal - Hard για τον 1ο computer παίκτη

        Επιστρέφει
        __________
        None
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
        Ελέγχει το ζευγάρι των παιχτών και ορίζει την couples.
        Έπειτα δημιουργεί ένα αντικείμενο Game() και καλεί την μέθοδο του mainloop

        Παράμετροι
        __________
        None

        Επιστρέφει
        __________
        None
        """
        if type(self.player1) == Player and type(self.player2) == Player:
            self.couples = 1
        if type(self.player1) != Player and type(self.player2) != Player:
            self.couples = 3
        else:
            self.couples = 2
        self.game = Game()
        self.game.mainloop()

    def current_player(self):
        """
        ελέγχει τον counter και αν  είναι ζηγός ο παίχτης είναι ο player1 αλλιώς ο player2

        Παράμετροι
        __________
        None

        Επιστρέφει
        __________
        player1 or player2
        """
        if self.count % 2 == 0:

            return self.player1
        else:
            return self.player2

    def other_player(self):
        """
        επιστρέφει τον παίχτη που δεν παίζει αυτή τη στιγμή

        Παράμετροι
        __________
        None

        Επιστρέφει
        __________
        player1 or player2
        """
        if self.current_player() == self.player1:
            return self.player2
        else:
            return self.player1

    def new_game(self):
        """
        Αλλάζει τους counters και αδειάζει το tablo αν ο game_count δε διαιρείτε με το μηδέν
        δίνει στον count την τιμή 1 για να παίξει πρώτος ο δεύτερος παίκτης

        Παράμετροι
        __________
        None

        Επιστρέφει
        __________
        None
        """
        self.game_count += 1
        self.count = self.game_count % 2
        self.tablo.tablo[self.player1] = []
        self.tablo.tablo[self.player2] = []

    def check_for_winner(self):
        """
        ελέγχει αν ο παίχτης έχει συμπληρώσει κάποια νικητήρια στήλη

        Παράμετροι
        __________
        None

        Επιστρέφει
        __________
        True or False
        """
        for j in self.tablo.winning_series:
            if all(i in self.tablo.tablo[self.current_player()] for i in j):
                return True
        else:
            return False

    def check_for_draw(self):
        """
        Ελέγχει αν έχουν παιχτεί όλες οι θέσεις

        Παράμετροι
        __________
        None

        Επιστρέφει
        __________
        True or False
        """

        if len(self.tablo.played()) == 9:
            return True
        else:
            return False

    def click_for_computer(self):
        """
        Προσπαθεί να παίξει για τον υπολογιστή αν ο παίχτης είναι human
        επιστρέφει None οπότε αποτυγχάνει και δεν κάνει κάτι
        """

        if not self.check_for_winner() or not self.check_for_draw():
            if self.couples == 3:
                time.sleep(1)
            try:
                eval('self.game.label{}_click("<Button-1>")'.format(
                    self.current_player().play(self.tablo)))
            except:
                pass

    def check(self, number, label, game):
        """
        ελέγχει αν το επιλεγμένο κελί έχει παιχτεί οπότε και εμφανίζει μήνυμα.
        αν όχι ελέγχει ποιός παίχτης έπαιξε καλεί την tablo.place_move για να τοποθετήσει την κίνηση στο tablo,
        δίνει το αντίστοιχο text στο label (Χ ή Ο)
        Ελέγχει αν υπάρχει νικητής ή ισοπαλία και αν ναι καλεί την open_winner μέθοδο του Game αντικειμένου
        αν όχι αυξάνει τον count αλλάζει το όνομα του παίχτη στο label_now_plays ώστε να δείχνει τον παίχτη που
        έχει σειρά να παίξει και καλεί τη μέθοδο click_for_computer η οποία αν ο επόμενος παίχτης είναι human περιμένει
        να πατήσει κάποιο label ο χρήστης

        Παράμετροι
        ----------
        number: int (1 to 9)
            αριθμός που δηλώνει τη θέση που έπαιξε ο παίχτης
        label: Game.label'n'
            το label στο οποίο έγινε η κίνηση
        game: Game()

        Επιστρέφει
        ----------
        None
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
        Βρίσκει ποια είναι η νικητήρια σειρά και χρωματίζει κόκκινο το κείμενο στα labels

        Παράμετροι
        ----------
        None

        Επιστρέφει
        ----------
        None
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
        Θυγατρική κλάση της Thread για την εκτέλεση κώδικα σε ξεχωριστό tread ωστε να ανανεώνεται
        το παράθυρο του παιχνιδιού όταν και οι δύο παίχτες είναι ο υπολογιστής.

        Πεδία
        ----------

        Μέθοδοι
        ----------
        run()
           Εντολή που θα τρέξουμε στο Thread
        """

    def __init__(self, game):
        super().__init__()
        self.game = game

    def run(self):
        """
        Αντικαθιστά τη run του parent με τον κώδικα που θέλουμε να εκτελέσουμε στο thread
        ο οποίος καλεί τη μέθοδο click_for_computer του αντικειμένου τύπου GameController που
        δημιουργήσαμε

        Παράμετροι
        ----------

        Επιστρέφει
        ----------
        """
        gc.click_for_computer()


class App(tk.Tk):
    """
        Αρχικό παράθυρο συλογής πληροφοριών

        Πεδία
        ----------
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

        Μέθοδοι
        ----------
        button_push()
            συμβάν κατά το πάτημα του submit_button
            δημιουργεί ένα global αντικείμενο GameControler, ελέγχει αν έχουν πληκτρογηθεί ονόματα και αν οχι
            βάζει σαν default τα Player1 & Player2 και στη συμέχεια καλή την get_settings μέθοδο
            αυτού όπου και τοποθετεί τα πεδία που συμπληρώσαμε. στη συνέχεια καταστρέφει τον εαυτό της
            και καλεί την game_by_couple() του διαχειριστή του παιχνιδιού.
    """

    def __init__(self):
        super().__init__()
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
        global gc
        gc = GameController()
        if self.player1_entry.get() == "":
            self.player1_entry.insert(0, "Player1")
        if self.player2_entry.get() == "":
            self.player2_entry.insert(0, "Player2")
        gc.get_settings(self.player1_entry.get(), self.player2_entry.get(), self.cd1.get(), self.cd2.get(),
                        self.selected_level1.get(), self.selected_level2.get())
        self.destroy()
        gc.game_by_couple()


class Game(tk.Tk):
    """
        Παράθυρο παιχνιδιού
        κατά την αρχικοποίηση καλεί τις μεθόδους geometry(ορίζει το μέγεθος και την θέση του παραθύρου),
        title(λεκτικό για τον τίτλο του παραθύρου), resizable(δεν επιτρέπει την αλλαγή των διαστάσεων
        του παραθύρου), ελέγχει αν παίζουν δύο υπολογιστές και αν ναι δημιουργεί ένα αντικείμενο
        PlayTwoComputers και καλεί την μέθοδο του run().
        Αν δεν παίζουν 2 υπολογιστές ελέγχει αν παίζει human και αν όχι εκτελεί την κίνηση του υπολογιστή

        Πεδία
        ----------

        camvas : tk.Canvas
           Η περιοχή παιχνιδιού όπου θα σχεδιαστούν οι γραμμές
        label1 : tk.Label
            label για την πάνω αριστερή θέση
        label2 : tk.Label
            label για την πάνω μεσαία θέση
        label3 : tk.Label
            label για την πάνω δεξιά θέση
        label4 : tk.Label
            label για την μεσαία αριστερή θέση
        label5 : tk.Label
            label για την κεντρική θέση
        label6 : tk.Label
            label για την μεσαία δεξιά θέση
        label7 : tk.Label
            label για την κάτω αριστερή θέση
        label8 : tk.Label
            label για την κάτω μεσαία θέση
        label9 : tk.Label
            label για την κάτω δεξιά θέση
        label_now_plays : ttk.Label
            Εμφανίζει τον παίκτη που πρέπει να παίξει
        score_board_label : tk.Label
            Τίτλος για το σκορ
        score_board_p1 : tk.Label
            Το όνομα του player1
        score_board_p2 : tk.Label
            Το όνομα του player2
        score_board_p1score : tk.Label
            To score του player1
        score_board_p2score : tk.Label
            To score του player2
        Στα label1, label2, label3, label4, label5, label6, label7, label8, label9 η μέθοδος bind
        ενεργοποιείται μόνο αν τουλάχιστον ένας παίκτης είναι human έτσι ώστε αν οι παίχτες είναι και οι δύο computer
        να μήν δέχεται κινήσεις από τον χρήστη.
        τα labels τα τοποθετούμε με συντεταγμένες ώστε να τοποθετηθούν πάνω στο camvas και να μήν καλύπτουν τις γραμμές

        Μέθοδοι
        ----------
        open_winner()
            καλεί το TopLevel Winner
        label1_click(event)
            καλεί την check την εκτελεί με παράμετρο τον αριθμό του κελιού και το label
        το ίδιο για κάθε labelx_click()
       """

    def __init__(self):
        super().__init__()
        self.geometry("+50+50")
        self.title('TikTakToe')
        self.resizable(False, False)

        self.camvas = tk.Canvas(self, width=250, height=215)
        self.camvas.create_line(90, 0, 90, 215, width=4, fill="grey")
        self.camvas.create_line(165, 0, 165, 215, width=4, fill="grey")
        self.camvas.create_line(20, 72, 230, 72, width=4, fill="grey")
        self.camvas.create_line(20, 142, 230, 142, width=4, fill="grey")
        self.camvas.grid(column=0, columnspan=2, row=0, pady=(10,20))
        self.label1 = tk.Label(self.camvas, text="", font=("Arial", 40), width=2)
        self.label1.place(x=20, y=2, width=65, height=65)
        if gc.couples != 3:
            self.label1.bind("<Button-1>", self.label1_click)
        self.label2 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label2.place(x=95, y=2, width=65, height=65)
        if gc.couples != 3:
            self.label2.bind("<Button-1>", self.label2_click)
        self.label3 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label3.place(x=170, y=2, width=65, height=65)
        if gc.couples != 3:
            self.label3.bind("<Button-1>", self.label3_click)
        self.label4 = tk.Label(self.camvas, font=("Arial", 40), width=2)
        self.label4.place(x=20, y=74, width=65, height=65)
        if gc.couples != 3:
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
        self.label_now_plays.config(text="Now Plays: {}".format(gc.current_player().name))
        self.label_now_plays.grid(column=0, columnspan=2, row=1, padx=(0, 0), sticky=tk.N)
        self.camvas_line1 = tk.Canvas(self,width=250, height=10)
        self.camvas_line1.create_line(0, 5, 250, 5, width=2, fill="grey")
        self.camvas_line1.grid(column=0, columnspan=2, row=2, pady=(5, 5))
        self.score_board_label = tk.Label(self, anchor="center", text="Score",
                                          font=("Arial", 15), width=15)
        self.score_board_label.grid(column=0, columnspan=2, row=3, sticky=tk.NSEW, padx=(0, 0), pady=(10, 0))

        self.label_x = tk.Label(self, borderwidth=2, text="X", font=("Arial", 20), width=1)
        self.label_x.grid(column=0, row=4, padx=(0, 0))
        self.label_y = tk.Label(self, borderwidth=2, text="O", font=("Arial", 20), width=1)
        self.label_y.grid(column=1, row=4, padx=(0, 0))
        self.score_board_p1 = tk.Label(self, borderwidth=2, text=f"{gc.player1.name}",
                                       font=("Arial", 12), width=20)
        self.score_board_p1.grid(column=0, row=5, padx=(0, 0))
        self.score_board_p2 = tk.Label(self, text=f"{gc.player2.name}", font=("Arial", 12), width=20)
        self.score_board_p2.grid(column=1, row=5, padx=(0, 0))
        self.camvas_line2 = tk.Canvas(self, width=250, height=10)
        self.camvas_line2.create_line(0, 5, 250, 5, width=2, fill="grey")
        self.camvas_line2.grid(column=0, columnspan=2, row=6, pady=(5, 5))
        self.score_board_p1score = tk.Label(self, text=f"{gc.score_board.board[gc.player1]}",
                                            font=("Arial", 15), width=8)
        self.score_board_p1score.grid(column=0, row=7, pady=(2, 30))
        self.score_board_p2score = tk.Label(self, text=f"{gc.score_board.board[gc.player2]}",
                                            font=("Arial", 15), width=8)
        self.score_board_p2score.grid(column=1, row=7, pady=(2, 30))

        # αν οι αντίπαλοι είναι δύο υπολογιστές δημιουργεί ένα Thread αντικείμενο (autoplay)
        # και καλεί τη start του αντικειμένου ώστε να εκτελεστούν οι κινήσεις χωρίς να διακοπεί η
        # επανάληψη του παραθύρου και να μπορούμε να της βλέπουμε τις κινήσεις στην οθόνη.
        if gc.couples == 3:
            autoplay = PlayTwoComputers(self)
            autoplay.start()
        # διαφορετικά αν ο παίκτης που παίζει είναι υπολογιστής καλεί τη μέθοδο play του παίχτη και
        # καλεί την bind του αντίστοιχου label.
        elif gc.current_player().play(gc.tablo) != 0:
            eval('self.label{}_click("<Button-1>")'.format(gc.current_player().play(gc.tablo)))

    def open_winner(self):
        Winner()

    def label1_click(self, event):
        gc.check(1, self.label1, self)

    def label2_click(self, event):
        gc.check(2, self.label2, self)

    def label3_click(self, event):
        gc.check(3, self.label3, self)

    def label4_click(self, event):
        gc.check(4, self.label4, self)

    def label5_click(self, event):
        gc.check(5, self.label5, self)

    def label6_click(self, event):
        gc.check(6, self.label6, self)

    def label7_click(self, event):
        gc.check(7, self.label7, self)

    def label8_click(self, event):
        gc.check(8, self.label8, self)

    def label9_click(self, event):
        gc.check(9, self.label9, self)


class Winner(tk.Toplevel):
    """
        Toplevel Παράθυρο Νικητή ή Ισοπαλίας
        κατά την σρχικοποίηση καλεί την grab_set() ώστε ο χρήστης να μην μπορεί να κάνει κίνηση στο
        Game Window

        Πεδία
        ----------
        label_winner : tk.Label
            Εμφανίζει τον τίτλο Νικη ή Ισοπαλία
        label_winner_name : tk.Label
            Αν έχουμε νικητή εμφανίζει το όνομα του
        label_score : tk.Label
            Τίτλος για το σκορ
        label_p1 : tk.Label
            Όνομα του player1
        label_p2 : tk.Label
            Όνομα του player2
        label_score_p1 : tk.Label
            Σκορ του player1
        label_score_p2 : tk.Label
            Σκορ του player2
        button_continue : tk.Label
            Κουμπί για συνέχεια του παιχνιδιού
        button_end : tk.Label
            Κουμπί για τερματισμό του παιχνιδιού

        Μέθοδοι
        ----------
        create_widgets()
            δημιουργεί τα στοιχεία του παραθύρου
        button_continue_push()
            καλεί την new_game() από το αντικείμενο τύπου GameController που δημιουργήσαμε
            καλεί την grap_release() για να ελευθερώσει το Game Window
            καταστρέφει το Game Window
            και καλεί την game_by_couple() από το αντικείμενο τύπου GameController που δημιουργήσαμε
        button_end_push()
            καταστρέφει το Game Window
       """

    def __init__(self):
        super().__init__()
        self.geometry("+400+350")
        self.title('TikTakToe')
        self.grab_set()
        self.resizable(False, False)
        # Ελέγχει αν υπάρχει νικητής ή είναι ισοπαλία το game και εμφανίζει το ανάλογο label
        # και το όνομα του νικητή αν υπάρχει
        if gc.check_for_winner():
            self.label_winner = tk.Label(self, text="The winner is:",
                                         font=("Arial", 13))
            self.label_winner.grid(column=0, row=0)
            self.label_winner_name = tk.Label(self, text=f"{gc.current_player().name}", font=("Arial", 19), width=24)
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
        gc.new_game()
        self.grab_release()
        gc.game.destroy()
        gc.game_by_couple()

    def button_end_push(self):
        gc.game.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()
