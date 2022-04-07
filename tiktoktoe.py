import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import game_play


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
        self.p1_iscom = ttk.Checkbutton(self, text='isComputer', variable= self.cd1)
        self.p1_iscom.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

        # player2
        player2_label = ttk.Label(self, text="Player2:")
        player2_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.player2_entry = ttk.Entry(self)
        self.player2_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # player2 = computer
        self.cd2 = tk.IntVar()
        self.p2_iscom = ttk.Checkbutton(self, text='isComputer', variable= self.cd2)
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
        # εδω βάζουμε τον κώδικα για να πάρουμε την επιλογή.
        print(self.selected_level.get())

    def button_push(self):
        game_play.game = game_play.Game_Play(self.player1_entry.get(), self.player2_entry.get(), self.cd1, self.cd2, self.selected_level.get())
        game_play.game.count = 0
        game_play.game.game_count = 0
        Game()
        App.destroy(self)

class Winner(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("270x270")
        self.title('TikTakToe')
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        if game_play.game.check_for_draw():
            self.label_winner = tk.Label(self, borderwidth=2, relief="groove", text="The Game is DRAW",
                                         font=("Arial", 12), width=30)
        else:
            self.label_winner = tk.Label(self,borderwidth=2, relief="groove", text="The winner is:",
                                         font=("Arial", 12), width=30)
            self.label_winner_name = tk.Label(self, borderwidth=2, relief="groove",
                                              text=f"{game_play.game.current_player()}", font=("Arial", 12), width=12)
            self.label_winner_name.grid(column=0, columnspan=4, row=1)
        self.label_winner.grid(column=0,columnspan=4, row=0)
        self.label_score = tk.Label(self, borderwidth=2, relief="groove",
                                          text="The Score is", font=("Arial", 12), width=12)
        self.label_score.grid(column=0, columnspan=4, row=2, pady=(5,0))
        self.label_p1 = tk.Label(self, borderwidth=2, relief="groove",
                                          text=f"{game_play.game.p1_name}", font=("Arial", 12), width=12)
        self.label_p1.grid(column=0, columnspan=2, row=3)
        self.label_p2 = tk.Label(self, borderwidth=2, relief="groove",
                                 text=f"{game_play.game.p2_name}", font=("Arial", 12), width=12)
        self.label_p2.grid(column=2, columnspan=2, row=3)
        self.label_score_p1 = tk.Label(self, borderwidth=2, relief="groove",
                                 text=f"{game_play.game.score_board[game_play.game.p1_name]}",
                                       font=("Arial", 12), width=12)
        self.label_score_p1.grid(column=0, columnspan=2, row=4)
        self.label_score_p2 = tk.Label(self, borderwidth=2, relief="groove",
                                 text=f"{game_play.game.score_board[game_play.game.p2_name]}",
                                 font=("Arial", 12), width=12)
        self.label_score_p2.grid(column=2, columnspan=2, row=4)
        self.button_continue = ttk.Button(self, command=self.button1_push, text="Continue")
        self.button_continue.grid(column=0, row=5, sticky=tk.E, padx=1, pady=1)
        self.button_end = ttk.Button(self, command=self.button2_push, text="End")
        self.button_end.grid(column=3, row=5, sticky=tk.W, padx=1, pady=1)

    def button1_push(self):
        game_play.game.game_count += 1
        game_play.game.count = game_play.game.game_count%2
        game_play.game.tablo[game_play.game.p1_name] = []
        game_play.game.tablo[game_play.game.p2_name] = []
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

    def create_widgets(self):
        # username

        self.label1 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label1.grid(column=0, row=0,padx=(110,0), sticky=tk.W)
        self.label1.bind("<Button-1>", self.label1_click)
        self.label2 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label2.grid(column=1, row=0, sticky=tk.W)
        self.label2.bind("<Button-1>", self.label2_click)
        self.label3 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label3.grid(column=2, row=0, sticky=tk.W)
        self.label3.bind("<Button-1>", self.label3_click)
        self.label4 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label4.grid(column=0,padx=(110,0), row=1, sticky=tk.W)
        self.label4.bind("<Button-1>", self.label4_click)
        self.label5 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label5.grid(column=1, row=1, sticky=tk.W)
        self.label5.bind("<Button-1>", self.label5_click)
        self.label6 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label6.grid(column=2, row=1, sticky=tk.W)
        self.label6.bind("<Button-1>", self.label6_click)
        self.label7 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label7.grid(column=0,padx=(110,0), row=2, sticky=tk.W)
        self.label7.bind("<Button-1>", self.label7_click)
        self.label8 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label8.grid(column=1, row=2, sticky=tk.W)
        self.label8.bind("<Button-1>", self.label8_click)
        self.label9 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label9.grid(column=2, row=2, sticky=tk.W)
        self.label9.bind("<Button-1>", self.label9_click)
        self.label_now_plays = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 12), width=25)
        self.label_now_plays.config(text="Current Player: {}".format(game_play.game.current_player()))
        self.label_now_plays.grid(column=0, columnspan=4, row=3,padx=(40,0), sticky=tk.S)
        self.score_board_label = tk.Label(self, borderwidth=2, relief="groove",anchor="center", text="Πίνακας Score",
                                           font=("Arial", 15), width=16)
        self.score_board_label.grid(column=0, columnspan=3, row=6, sticky=tk.NSEW, padx=(80,0), pady=(10,0))
        self.score_board_p1 = tk.Label(self, borderwidth=2, relief="groove", text=f"{game_play.game.p1_name}",
                                        font=("Arial", 10), width=15)
        self.score_board_p1.grid(column=0, columnspan=2, row=7)
        self.score_board_p2 = tk.Label(self, borderwidth=2, relief="groove", text=f"{game_play.game.p2_name}",
                                        font=("Arial", 10), width=15)
        self.score_board_p2.grid(column=2, columnspan=2, row=7)
        self.score_board_p1score = tk.Label(self, borderwidth=2, relief="groove",
                                            text=f"{game_play.game.score_board[game_play.game.p1_name]}",
                                            font=("Arial", 15), width=11)
        self.score_board_p1score.grid(column=0, columnspan=2, row=8)
        self.score_board_p2score = tk.Label(self, borderwidth=2, relief="groove",
                                            text=f"{game_play.game.score_board[game_play.game.p2_name]}",
                                            font=("Arial", 15), width=11)
        self.score_board_p2score.grid(column=2, columnspan=2, row=8)

    def check(self, number, label):
        if number not in game_play.game.tablo[game_play.game.p1_name] + game_play.game.tablo[game_play.game.p1_name]:
            if game_play.game.current_player() == game_play.game.p1_name:
                game_play.game.tablo[game_play.game.p1_name].append(number)
                label.config(text='X')
                if game_play.game.check_for_winner() or game_play.game.check_for_draw():
                    if game_play.game.check_for_winner():
                        game_play.game.score_board[game_play.game.current_player()] += 1
                    Game.destroy(self)
                    Winner()
                game_play.game.count += 1
                self.label_now_plays.config(text="Current Player: {}".format(game_play.game.current_player()))


            else:
                game_play.game.tablo[game_play.game.p2_name].append(number)
                label.config(text='O')
                if game_play.game.check_for_winner() or game_play.game.check_for_draw():
                    if game_play.game.check_for_winner():
                        game_play.game.score_board[game_play.game.current_player()] += 1
                    Game.destroy(self)
                    Winner()
                game_play.game.count += 1
                self.label_now_plays.config(text="Current Player: {}".format(game_play.game.current_player()))




            print(game_play.game.tablo, game_play.game.count)
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')


    def label1_click(self, event):
        self.check(1, self.label1)

    def label2_click(self, event):
        self.check(2, self.label2)

    def label3_click(self, event):
        self.check(3, self.label3)

    def label4_click(self, event):
        self.check(4, self.label4)

    def label5_click(self, event):
        self.check(5, self.label5)

    def label6_click(self, event):
        self.check(6, self.label6)

    def label7_click(self, event):
        self.check(7, self.label7)

    def label8_click(self, event):
        self.check(8, self.label8)

    def label9_click(self, event):
        self.check(9,self.label9)

if __name__ == "__main__":
    app = App()
    app.mainloop()