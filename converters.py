while True:
    choice = int(input(
        "ENTER\n1 for kilometers to miles \n2 for miles to kilometers\n3 for celsius to fahrenheit\n"
        "4 for fahrenheit to celsius\n5 for BMI Calculator"))
    if choice == 1:
        km = float(input("enter how much kilometers"))


        def kmtomiles(km):
            return km / 1.6


        print(km, " kilometers is equal to = ", kmtomiles(km), " miles")
    if choice == 2:
        miles = (float(input("enter how much miles")))


        def milestokm(miles):
            return miles * 1.6


        print(miles, " miles is equal to = ", milestokm(miles), " kilometers")
    if choice == 3:
        celsius = (float(input("enter how many celsius")))


        def celtofah(celsius):
            return (celsius * 9 // 5) + 32


        print(celsius, "° celsius is equal to = ", celtofah(celsius), "° fahrenheit")
    if choice == 4:
        fahrenheit = (float(input("enter how many fahrenheit")))


        def fahtocel(fahrenheit):
            return (fahrenheit - 32) * 5 // 9


        print(fahrenheit, "° fahrenheit is equal to = ", fahtocel(fahrenheit), "° celsius")
    if choice == 5:
        weight = float(input("Enter your weight in KGs"))
        height = float(input("enter your height in CMs"))


        def bmi(weight, height):
            return weight / ((height / 100) * (height / 100))


        print("your BMI is", ("{:.1f}".format(bmi(weight, height))))
        #print("{:.1f}".format(number)) for 2 decimals
        if bmi(weight, height) < 18.5:
            print("You are underweight")
        if bmi(weight, height) > 18.5 and bmi(weight,height) < 24.9:
            print("You are in normal weight")
        if bmi(weight, height) > 25 and bmi(weight, height) < 29.9:
            print("You are overweight")
        if bmi(weight, height) > 30:
            print("You are obese")
    pa = input("again?(yes/no)")
    if pa == "no":
        print("THANK YOU")
        break
