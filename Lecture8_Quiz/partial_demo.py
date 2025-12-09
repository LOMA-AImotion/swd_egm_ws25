import tkinter
from tkinter import messagebox
from functools import partial

main_win = tkinter.Tk() 

def show_info_box(num):
    messagebox.showinfo("Hi", f"You pressed {num}")
    
number = 1
for row in range(3):
    for col in range(3):
        button = tkinter.Button(main_win, text=str(number))
        button.grid(row=row, column = col)        
        button.config( height = 5, width = 10)
        button.config(command = partial(show_info_box, number))
        partial(show_info_box, 1)
        partial(show_info_box, 2)
        number += 1
main_win.mainloop()
