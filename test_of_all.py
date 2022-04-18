#
#
# import tkinter as tk
# import time
# from threading import *
#
#
#
#
# class App(tk.Tk):
#
#     def __init__(self):
#         super().__init__()
#         self.geometry("450x150")
#         self.title('Tik Tok Toe')
#         self.create_widgets()
#
#     def create_widgets(self):
#         # player1
#         self.player1_label = tk.Label(self, text="Player1:")
#         self.player1_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
#         submit_button = tk.Button(self, command=self.threading, text="Submit")
#         submit_button.grid(column=2, row=4, sticky=tk.S, padx=5, pady=5)
#
#     def threading(self):
#         t1 = Thread(target=self.auto_play())
#         t1.start()
#
#     def auto_play(self):
#         for i in range(10):
#             self.player1_label.config(text=i)
#             time.sleep(1)


from tkinter import *
import time
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")


# use threading

def threading():
    # Call work function
    t1 = Thread(target=work)
    t1.start()


# work function
def work():

    for i in range(10):
        button.config(text=i)
        time.sleep(1)



# Create Button
button = Button(root, text="Click Me", command=threading)
button.pack()

# Execute Tkinter
root.mainloop()

#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
