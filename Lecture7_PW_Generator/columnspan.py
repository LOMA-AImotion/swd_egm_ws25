import tkinter

main_win = tkinter.Tk()
main_win.title("THI")
canvas = tkinter.Canvas(main_win, width=600, height = 300)
canvas.grid(columnspan=3, rowspan=4)

label = tkinter.Label(main_win, text="This is a label")
label.grid(row=0, column=0, columnspan=2)
button = tkinter.Button(main_win, text="B1")
button.grid(row=1, column=0)
button2 = tkinter.Button(main_win, text="B2")
button2.grid(row=1, column=1)
main_win.mainloop()