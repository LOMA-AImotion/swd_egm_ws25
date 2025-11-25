import tkinter

main_win = tkinter.Tk()
main_win.title("EGM SWD")
label = tkinter.Label(main_win, text="Hello from inside our first GUI!!!")
label.pack()

button = tkinter.Button(main_win, text="NO")
button.pack()
button2 = tkinter.Button(main_win, text="YES")
button2.pack()

main_win.mainloop()

print("Hello from after mainloop()")
