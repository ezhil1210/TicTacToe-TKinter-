from random import randint
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="#373737")
win = LabelFrame(root, text="ROCK PAPER SCISSORS by Ezhil", bg='#373737', fg="orange", padx=20, pady=20)
win.pack(padx=20, pady=20)
rock = PhotoImage(file='C:/Users/USER/OneDrive/Pictures/rps/pc rock.png')
paper = PhotoImage(file='C:/Users/USER/OneDrive/Pictures/rps/pc paper.png')
scissors = PhotoImage(file='C:/Users/USER/OneDrive/Pictures/rps/pc scissors.png')
you = Label(win, text="YOU", font=('Helvetica', 18, 'bold'), bg="#373737",fg="green").grid(row=1, column=0)
computerlabel = Label(win, text="COMPUTER", font=('Helvetica', 18, 'bold'), bg="#373737",fg="green").grid(row=1, column=2)
image_list = [rock, paper, scissors]
computer = randint(0, 2)
computerimage = Label(win, image=image_list[0], height=350, width=300, padx=60)
computerimage.grid(row=2, column=2)

userscore = 0
computerscore = 0
result = Label(win, text="", font=('Helvetica', 18, 'bold'), bg="#373737", fg="orange", justify="center")
result.grid(row=7, column=0, columnspan=3)
score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737", fg="#00C0FF")
score.grid(column=1, row=9)
userimage = PhotoImage(file='C:/Users/USER/OneDrive/Pictures/rps/user rock.png')
userpicture = Label(win, image=userimage, height=350, width=300, padx=60, bd=0)
userpicture.grid(row=2, column=0)


def clickrock():
    global userscore, computerscore
    computer = randint(0, 2)
    computerimage.config(image=image_list[computer])
    userimage.config(file='C:/Users/USER/OneDrive/Pictures/rps/user rock.png')
    if computer == 0:
        result.config(text="It's a tie!",fg="orange")
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)
    elif computer == 1:
        result.config(text="Paper covers rock!. You Lose!",fg="orange")
        computerscore += 1
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)
    elif computer == 2:
        result.config(text="Rock smashes scissors!. You win!", fg="orange")
        userscore += 1


score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737", fg="#00C0FF")
score.grid(column=1, row=9)

Rock = Button(win, text="Rock", font=('Helvetica', 18, 'bold'), command=clickrock, bg="#373737", fg="purple")
Rock.grid(row=6, column=0)


def clickpaper():
    global userscore, computerscore
    computer = randint(0, 2)
    computerimage.config(image=image_list[computer])
    userimage.config(file='C:/Users/USER/OneDrive/Pictures/rps/user paper.png')
    if computer == 1:
        result.config(text="It's a tie!")
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)
    elif computer == 0:
        result.config(text="Paper covers rock!. You Win!")
        userscore += 1
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)
    elif computer == 2:
        result.config(text="Scissors cuts paper!. You lose!")
        computerscore += 1
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)


Paper = Button(win, text="Paper", font=('Helvetica', 18, 'bold'), command=clickpaper, bg="#373737", fg="green")
Paper.grid(row=6, column=1)


def clickscissor():
    global computerscore, userscore
    computer = randint(0, 2)
    computerimage.config(image=image_list[computer])
    userimage.config(file='C:/Users/USER/OneDrive/Pictures/rps/user scissors.png')
    if computer == 0:
        result.config(text="Rock smashes scissors!. You Lose!")
        computerscore += 1
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)
    elif computer == 1:
        result.config(text="Scissors cuts paper!. You Win!")
        userscore += 1
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)
    elif computer == 2:
        result.config(text="It's a tie!")
        score = Label(win, text=(userscore, "-", computerscore), font=('Helvetica', 18, 'bold'), bg="#373737",
                      fg="#00C0FF")
        score.grid(column=1, row=9)


Scissors = Button(win, text="Scissors", font=('Helvetica', 18, 'bold'), command=clickscissor, bg="#373737",
                  fg="orange")
Scissors.grid(row=6, column=2)
win.mainloop()