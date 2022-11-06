from tkinter import *
from tkinter import ttk

win = Tk()
win.title("gui calc")
win.config(bg="#373737")
win.resizable(0, 0)

root = LabelFrame(win, text="Calculator By Ezhil", bg='#373737', fg="white", padx=20, pady=20)
root.pack(padx=20, pady=20)
e = Entry(root, width=25, font=('arial', 18, 'bold'), borderwidth=5, text="0", justify='right', bg="#373737", fg="white")
e.insert(0, 0)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):

    current = e.get()

    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def Button_Clear():
    e.delete(0, END)
    e.insert(0, 0)


def Button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def Button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def Button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def Button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def Button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


button_1 = Button(root, text=1, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(1))
button_2 = Button(root, text=2, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(2))
button_3 = Button(root, text=3, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(3))
button_4 = Button(root, text=4, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(4))
button_5 = Button(root, text=5, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(5))
button_6 = Button(root, text=6, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(6))
button_7 = Button(root, text=7, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(7))
button_8 = Button(root, text=8, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(8))
button_9 = Button(root, text=9, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(9))
button_0 = Button(root, text=0, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(0))
button_add = Button(root, text="+", font="bold", padx=40, pady=20, bg="#373737", fg="orange", command=Button_add)
button_equal = Button(root, text="=", font="bold", padx=100, pady=20, bg="#373737", fg="green", command=Button_equal)
button_clear = Button(root, text="C", font="bold", padx=99, pady=20, bg="#373737", fg="orange", command=Button_Clear)
button_sub = Button(root, text="-", font="bold", padx=42, pady=20, bg="#373737", fg="orange", command=Button_sub)
button_mul = Button(root, text="×", font="bold", padx=40, pady=20, bg="#373737", fg="orange", command=Button_mul)
button_div = Button(root, text="÷", font="bold", padx=40, pady=20, bg="#373737", fg="orange", command=Button_div)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_clear.grid(row=6, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=4, column=2)
button_mul.grid(row=5, column=0)
button_div.grid(row=6, column=0)

win.mainloop()
