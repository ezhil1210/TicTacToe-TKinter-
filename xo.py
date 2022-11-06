from tkinter import *
from tkinter import messagebox
import random
from random import randint

root = Tk()
root.title('XO')
root.configure(bg="#373737")
root.resizable(0, 0)
clicked = True
x = 0
o = 0
r = IntVar()
r.set("2")
win = LabelFrame(root, text="Tic-Tac-Toe by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
win.pack(padx=20, pady=20)
e = Entry(win, width=25, font=('arial', 18, 'bold'), borderwidth=5, text="Enter your e.get", justify='right', bg="#373737",
          fg="white")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def get():
    global name
    playername = e.get()
    name = str(playername)
    reset()

getplayername = Button(win, text="Play", command=get, bg="#373737", fg="orange")
getplayername.grid(row=4, column=1, pady=20)
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b7, b8, b8, b9, score, e, name
    global clicked, count, buttons
    clicked = True
    count = 0
    for widget in win.winfo_children():
        widget.destroy()
    playername = e.get
    b1 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b1))
    b2 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b2))
    b3 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b3))
    b4 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b4))
    b5 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b5))
    b6 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b6))
    b7 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b7))
    b8 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b8))
    b9 = Button(win, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    Radiobutton(win, text=(name ,"vs PLAYER"), bg="#373737", fg="red", font=('Helvetica', 10, 'bold'), variable=r,
                value=1).grid(row=0, column=4)
    Radiobutton(win, text= (name,"vs COMPUTER"), bg="#373737", fg="red", font=('Helvetica', 10, 'bold'), variable=r,
                value=2).grid(row=1, column=4)
    resetbtn = Button(win, text="Reset Game", command=reset, bg="#373737", fg="orange").grid(row=4, column=1, pady=20)
    score = Label(win, text=(x, "-", o), bg="#373737", fg="light blue", font=('Helvetica', 18, 'bold'))
    score.grid(row=3, column=1, pady=20)







def b_click(b):
    global clicked, count, buttons
    type = r.get()
    if b["text"] == " " and clicked == True:
        b.config(text="X", fg="green")
        clicked = False
        buttons.remove(b)
        count += 1
        checkifwon()

    if type == 1 and b["text"] == " " and clicked == False:
        b.config(text="O", fg="orange")
        clicked = True
        buttons.remove(b)
        count += 1
        checkifwon()

    if type == 2 and clicked == False:
        computerchoice = random.choice(buttons)
        computerchoice.config(text="O", fg="orange")
        buttons.remove(computerchoice)
        clicked = True
        count += 1
        checkifwon()


def checkifwon():
    global winner, x, o, score
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red", fg="green")
        b2.config(bg="red", fg="green")
        b3.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        b6.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red", fg="green")
        b8.config(bg="red", fg="green")
        b9.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b7.config(bg="red", fg="green")
        b4.config(bg="red", fg="green")
        b1.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        b8.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red", fg="green")
        b6.config(bg="red", fg="green")
        b9.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        b9.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    elif b7["text"] == "X" and b3["text"] == "X" and b5["text"] == "X":
        b7.config(bg="red", fg="green")
        b3.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "X Won!")
        reset()
        x += 1
        score.config(text=(x, "-", o))
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red", fg="green")
        b2.config(bg="red", fg="green")
        b3.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        b6.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red", fg="green")
        b8.config(bg="red", fg="green")
        b9.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b7.config(bg="red", fg="green")
        b4.config(bg="red", fg="green")
        b1.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        b8.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red", fg="green")
        b6.config(bg="red", fg="green")
        b9.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        b9.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    elif b7["text"] == "O" and b3["text"] == "O" and b5["text"] == "O":
        b7.config(bg="red", fg="green")
        b3.config(bg="red", fg="green")
        b5.config(bg="red", fg="green")
        winner = True
        messagebox.showinfo("Match Result", "O Won!")
        reset()
        o += 1
        score.config(text=(x, "-", o))
    if count == 9 and winner == False:
        messagebox.showinfo("Match Result", " It's a tie!")
        reset()
        score.config(text=(x, "-", o))


win.mainloop()
