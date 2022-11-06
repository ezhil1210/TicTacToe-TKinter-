import random

action = ["rock", "paper", "scissor"]
userscore = 0
computerscore = 0
response = input("HI DUDE! CAN WE PLAY A GAME ?(yes/no)")
if response == "no":
    print("OK DUDE")
if response == "yes":
    while True:
        user = int(
            input("OK DUDE . LETS PLAY ROCK PAPER SCISSORS\n\n"
                  "ENTER \n 1 for rock\n 2 for paper\n 3 for scissor"))
        computer = random.choice(action)
        if user == 1:
            print("you chose rock the computer chose", computer)
            if computer == "rock":
                print("ROCK - ROCK\nDRAW")
                print(userscore, "-", computerscore)
            if computer == "paper":
                print("ROCK - PAPER \nCOMPUTER WINS")
                computerscore += 1
                print(userscore, "-", computerscore)
            if computer == "scissor":
                print("ROCK - scissor \nYOU WIN")
                userscore += 1
                print(userscore, "-", computerscore)
        elif user == 2:
            print("you chose paper the computer chose", computer)
            if computer == "rock":
                print("PAPER - ROCK \nYOU WIN")
                userscore += 1
                print(userscore, "-", computerscore)
            if computer == "paper":
                print("PAPER - PAPER \nDRAW")
                print(userscore, "-", computerscore)
            if computer == "scissor":
                print("PAPER - scissor \nCOMPUTER WINS")
                computerscore += 1
                print(userscore, "-", computerscore)
        elif user == 3:
            print("you chose scissor the computer chose", computer)
            if computer == "rock":
                print("SCISSOR - ROCK \nCOMPUTER WINS")
                computerscore += 1
                print(userscore, "-", computerscore)
            if computer == "paper":
                print("SCISSOR - PAPER \nYOU WIN")
                userscore += 1
                print(userscore, "-", computerscore)
            if computer == "scissor":
                print("SCISSOR - SCISSOR \nDRAW")
                print(userscore, "-", computerscore)
        else:
            print("enter only 1,2 and 3")

        pa = input("again?(yes/no)")
        if pa == "no":
            break
    print("The final score is ")
    print(userscore, "-", computerscore)

    if userscore < computerscore:
        print("YOU LOST")
    if userscore == computerscore:
        print("MATCH DRAWN")
    if userscore > computerscore:
        print("YOU WON")
    print("k dude see you later")
