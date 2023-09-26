from tkinter import *
root = Tk()
root.title("Converters")
root.configure(bg="#373737")
root.geometry("560x610")
root.resizable(0, 0)

win = LabelFrame(root, text="", bg='#373737', width=540, height=520, fg="orange", padx=34,
                 pady=20)

win.grid(row=0, column=0, padx=20, pady=20)

def home():
    global homebtn

    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Converters App By Ezhil")
    alal = Label(win, bg="#373737", fg="light green", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               \n  Click any button for conversion    ",
                 justify="left").grid(row=0, column=0)
    kmmbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                    text="Kilometer to Meter", command=kmmpage)
    kmmbtn.grid(row=1, column=0, padx=20, pady=15)
    mkmbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                    text="Meter to Kilometer", command=mkmpage)
    mkmbtn.grid(row=2, column=0, padx=20, pady=15)
    ftcbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=22, pady=5, fg="#00C0FF",
                    text="Fahrenheit to Celcius", command=fahcel)
    ftcbtn.grid(row=3, column=0, padx=20, pady=15)
    ctfbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=22, pady=5, fg="#00C0FF",
                    text="Celcius to Fahrenheit", command=celfah)
    ctfbtn.grid(row=4, column=0, padx=20, pady=15)
    milekmbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                       text="Miles to Kilometers", command=milekmpage)
    milekmbtn.grid(row=5, column=0, padx=20, pady=15)
    kmmilebtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                       text="Kilometers to Miles", command=kmmilepage)
    kmmilebtn.grid(row=6, column=0, padx=20, pady=15)
    bmibtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                       text="Calculate your BMI", command=bmipage)
    bmibtn.grid(row=7, column=0, padx=20, pady=15)
def hombtn():
    homebtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid()
def kmmpage():
    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Convert Kilometers to Meters")
    alal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter KM value    ",
                 justify="left").grid(row=0, column=0)

    Km = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
               fg="white")

    Km.grid(row=1, column=0)
    label = Label(win, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
    label.grid(row=2, column=0)

    def kmmfun():
        m = float(Km.get()) * 1000
        label.config(text=str(Km.get()) + "KM = " + str(round(m, 2)) + "meters")

    kmmconbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Convert",
                       command=kmmfun)
    kmmconbtn.grid(row=3, column=0, padx=20, pady=15)
    hombtn()
def mkmpage():
    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Convert Meters to Kilometers")
    alal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter Meters value    ",
                 justify="left").grid(row=0, column=0)

    meters = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                   fg="white")

    meters.grid()
    label = Label(win, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
    label.grid()

    def mkmfun():
        kilom = float(meters.get()) / 1000
        label.config(text=str(meters.get()) + " meters = " + str(round(kilom, 2)) + " KM")

    mkmconbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Convert",
                       command=mkmfun)
    mkmconbtn.grid(padx=20, pady=15)
    hombtn()
def fahcel():
    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Convert Fahrenheit to Celsius")
    alal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter Fahrenheit value    ",
                 justify="left").grid(row=0, column=0)

    fah = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                fg="white")
    fah.grid()
    label = Label(win, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
    label.grid()

    def fahceldef():
        celcius = (float(fah.get()) - 32) * 5 / 9
        label.config(text=str(fah.get()) + " fahrenheit = " + str(round(celcius, 2)) + " celcius")

    ftcconbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Convert",
                       command=fahceldef)
    ftcconbtn.grid(padx=20, pady=15)
    hombtn()
def celfah():
    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Convert Celcius to Fahrenheit")
    alal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter Celcius value    ",
                 justify="left").grid(row=0, column=0)

    cel = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                fg="white")

    cel.grid()
    label = Label(win, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
    label.grid()

    def celfahdef():
        fahreneit = (float(cel.get()) * 9 // 5) + 32
        label.config(text=str(cel.get()) + " celcius = " + str(round(fahreneit, 2)) + " fahrenheit")

    ctfconbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Convert",
                       command=celfahdef)
    ctfconbtn.grid(padx=20, pady=15)
    hombtn()
def milekmpage():
    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Convert Miles to Kilometers")
    alal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter Miles value    ",
                 justify="left").grid(row=0, column=0)

    miles = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                  fg="white")
    miles.grid()
    label = Label(win, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
    label.grid()

    def milekmfun():
        kilo = float(miles.get()) * 1.6
        label.config(text=str(miles.get()) + " miles = " + str(round(kilo, 2)) + " KM")

    milekmconbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                          text="Convert", command=milekmfun)
    milekmconbtn.grid(padx=20, pady=15)
    hombtn()
def kmmilepage():
    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Convert Kilometers to Meters")
    alal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter KM value    ",
                 justify="left").grid(row=0, column=0)

    kilometer = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                      fg="white")

    kilometer.grid()
    label = Label(win, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
    label.grid()

    def kmmilefun():
        mile = float(kilometer.get()) / 1.6
        label.config(text=str(kilometer.get()) + " KM = " + str(mile) + "Miles")
    kmmileconbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                          text="Convert", command=kmmilefun)
    kmmileconbtn.grid(padx=20, pady=15)
    homebtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                     command=home).grid(row=4,column=0,columnspan=4)
def bmipage():
    for widget in win.winfo_children():
        widget.destroy()
    win.config(text="Calculate your BMI")
    alal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter your weight in KGs    ",
                 justify="left").grid()

    weight = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right',
                   bg="#373737",
                   fg="white")
    weight.grid(pady=20)
    aeal = Label(win, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                 text="                                                                                                               "
                      "\n  Enter your height in CMs    ",
                 justify="left").grid()

    height = Entry(win, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right',
                   bg="#373737",
                   fg="white")
    height.grid(pady=20)
    label = Label(win, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
    label.grid()

    def bmifun():
        m = int(height.get())/100
        bmi = int(weight.get()) / (m*m)
        if bmi < 18.5:
            label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are underweight")
        if bmi > 18.5 and bmi < 24.9:
            label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are in normal weight")
        if bmi > 25 and bmi < 29.9:
            label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are overweight")
        if bmi > 30:
            label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are obese")
    bmiconbtn = Button(win, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                       text="Convert", command=bmifun)
    bmiconbtn.grid(padx=20, pady=15)
    hombtn()

home()

root.mainloop()
