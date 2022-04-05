import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class App(tk.Tk):
    x = []
    o = []
    now_play = 0
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title('Login')
        self.resizable(0, 0)


        self.create_widgets()

    def create_widgets(self):
        # username
        self.label1 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label1.grid(column=0, row=0, sticky=tk.W)
        self.label1.bind("<Button-1>", self.label1_click)
        self.label2 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label2.grid(column=1, row=0, sticky=tk.W)
        self.label2.bind("<Button-1>", self.label2_click)
        self.label3 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label3.grid(column=2, row=0, sticky=tk.W)
        self.label3.bind("<Button-1>", self.label3_click)
        self.label4 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label4.grid(column=0, row=1, sticky=tk.W)
        self.label4.bind("<Button-1>", self.label4_click)
        self.label5 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label5.grid(column=1, row=1, sticky=tk.W)
        self.label5.bind("<Button-1>", self.label5_click)
        self.label6 = ttk.Label(self,borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label6.grid(column=2, row=1, sticky=tk.W)
        self.label6.bind("<Button-1>", self.label6_click)
        self.label7 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label7.grid(column=0, row=2, sticky=tk.W)
        self.label7.bind("<Button-1>", self.label7_click)
        self.label8 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label8.grid(column=1, row=2, sticky=tk.W)
        self.label8.bind("<Button-1>", self.label8_click)
        self.label9 = ttk.Label(self, borderwidth=2, relief="groove", text="   ", font=("Arial", 40), width=2)
        self.label9.grid(column=2, row=2, sticky=tk.W)
        self.label9.bind("<Button-1>", self.label9_click)


    def label1_click(self, event):
        if 1 not in App.x + App.o:
            if App.now_play%2 == 0:
                App.x.append(1)
                self.label1.config(text='X')
                print(App.x)
                App.now_play +=1
            else:
                App.o.append(1)
                self.label1.config(text='O')
                print(App.o)
                App.now_play += 1

        else : messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')


    def label2_click(self, event):
        if 2 not in App.x + App.o:
            if App.now_play % 2 == 0:
                App.x.append(2)
                self.label2.config(text='X')
                print(App.x)
                App.now_play += 1
            else:
                App.o.append(2)
                self.label2.config(text='O')
                print(App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

    def label3_click(self, event):
        if 3 not in App.x  + App.o:
            if App.now_play % 2 == 0:
                App.x.append(3)
                self.label3.config(text='X')
                print(App.x)
                App.now_play += 1
            else:
                App.o.append(3)
                self.label3.config(text='O')
                print(App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

    def label4_click(self, event):
        if 4 not in App.x + App.o:
            if App.now_play % 2 == 0:
                App.x.append(4)
                self.label4.config(text='X')
                print(App.x)
                App.now_play += 1
            else:
                App.o.append(4)
                self.label4.config(text='O')
                print(App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

    def label5_click(self, event):
        if 5 not in App.x  + App.o:
            if App.now_play % 2 == 0:
                App.x.append(5)
                self.label5.config(text='X')
                print(App.x)
                App.now_play += 1
            else:
                App.o.append(5)
                self.label5.config(text='O')
                print(App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

    def label6_click(self, event):
        if 6 not in App.x  + App.o:
            if App.now_play % 2 == 0:
                App.x.append(6)
                self.label6.config(text='X')
                print(App.x)
                App.now_play += 1
            else:
                App.o.append(6)
                self.label6.config(text='O')
                print(App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

    def label7_click(self, event):
        if 7 not in App.x  + App.o:
            if App.now_play % 2 == 0:
                App.x.append(7)
                self.label7.config(text='X')
                print(App.x)
                App.now_play += 1
            else:
                App.o.append(7)
                self.label7.config(text='O')
                print(App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

    def label8_click(self, event):
        if '8' not in App.x  + App.o:
            if App.now_play % 2 == 0:
                App.x.append(8)
                self.label8.config(text='X')
                print(App.x)
                App.now_play += 1
            else:
                App.o.append(8)
                self.label8.config(text='O')
                print(App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

    def label9_click(self, event):
        if '9' not in App.x  + App.o:
            if App.now_play % 2 == 0:
                App.x.append(9)
                self.label9.config(text='X')
                print(App.x+App.o)
                App.now_play += 1
            else:
                App.o.append(9)
                self.label9.config(text='O')
                print(App.x+App.o)
                App.now_play += 1
        else:
            messagebox.showwarning(title='Wrong Choice', message='You have to chooce an empty place')

if __name__ == "__main__":
    app = App()
    app.mainloop()