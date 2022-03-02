import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x150")
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

        player1_entry = ttk.Entry(self)
        player1_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # player1 = computer
        p1_iscom = ttk.Checkbutton(self, text='isComputer', onvalue=None)
        p1_iscom.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

        # player2
        player2_label = ttk.Label(self, text="Player2:")
        player2_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        player2_entry = ttk.Entry(self)
        player2_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # player2 = computer
        p2_iscom = ttk.Checkbutton(self, text='isComputer', onvalue=None)
        p2_iscom.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

        # Computer Intelligence
        intell_label = ttk.Label(self, text='Computer Inteligence:  ')
        intell_label.grid(column=0, row=3, columnspan=2, sticky=tk.SE, padx=5, pady=5)

        self.selected_level = tk.StringVar()
        level = ('Easy', 'Normal')
        intell_choise = ttk.Combobox(self, textvariable=self.selected_level, values=level, state='readonly')
        intell_choise.bind('<<ComboboxSelected>>', self.level_changed)
        intell_choise.grid(column=2, row=3, sticky=tk.W)

        # submit button
        submit_button = ttk.Button(self, text="Submit")
        submit_button.grid(column=2, row=4, sticky=tk.S, padx=5, pady=5)



    def level_changed(self, event):
        # εδω βάζουμε τον κώδικα για να πάρουμε την επιλογή.
        print(self.selected_level.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
