def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


def squ(a):
    return a * a


def ave(a, b, c):
    return (a+b+c)/3


NAME = input("ENTER YOUR NAME")
print("hi", NAME)
while True:
    OPERATION = int(input(
    "WHAT OPERATION YOU WANT TO DO\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.SQUARE OF A NUMBER\n6."
    "AVERAGE OF THREE NUMBERS"))

    if OPERATION == 1:
        a = int(input("a = "))
        b = int(input("b = "))
        print("the value of \n", a, "+", b, "=", add(a, b), "\n THANK YOU")
    elif OPERATION == 2:
        a = int(input("a = "))
        b = int(input("b = "))
        print("the value of \n", a, "-", b, "=", sub(a, b), "\n THANK YOU")
    elif OPERATION == 3:
        a = int(input("a = "))
        b = int(input("b = "))
        print("the value of \n", a, "×", b, "=", mul(a, b), "\n THANK YOU")
    elif OPERATION == 4:
        a = int(input("a = "))
        b = int(input("b = "))
        print("the value of \n", a, "÷", b, "=", div(a, b), "\n THANK YOU")
    elif OPERATION == 5:
        a = int(input("a = "))
        print("the value of ", a, "² =", squ(a), "\n THANK YOU")
    elif OPERATION == 6:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        print("the average  of ", a, ",", b, "AND", c, " =", ave(a, b, c), "\n THANK YOU")
    next_calculation = input("Let's do next calculation? (yes/no)")
    if next_calculation == "no":
        break
else:
    print("WRONG INPUT. PLEASE TYPE 1 TO 6 ONLY")
