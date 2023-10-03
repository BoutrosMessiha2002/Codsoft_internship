
# A normal and simple calculator
"""
while True:
    number1=float(input("Enter first number: "))
    number2=float(input("Enter second number: "))
    symbol=input("Enter operation: ")
    result=None
    try:
        if symbol=='+':
            result=number1+number2
        elif symbol=='-':
            result=number1-number2
        elif symbol=='*':
            result=number1*number2
        elif symbol=='/':
            result=number1/number2
    except ZeroDivisionError:
        print("Cannot divide by 0")
    print(result)
    user_answer=input("Do you want to perform another operation? Yes/No: ")
    if user_answer=="No":
        print("Thanks for using the program")
        break
"""
# A calculator using GUI

from tkinter import*
def operation(symbol):
    global equation
    equation=equation+str(symbol)
    screen.set(equation)
def result():
    global equation
    try:
        total=str(eval(equation))
        screen.set(total)
        equation=""
    except ZeroDivisionError:
        screen.set("cannot divide by 0")
        equation=""

def clear():
    global equation
    screen.set("")
    equation=""


window=Tk()
window.config(bg="#f7fae1")
window.geometry("420x420")
screen=StringVar()
equation=""
label=Label(textvariable=screen,font=("Times New Roman",24),width=18)
label.pack()
frame=Frame(window)
frame.pack()
Number1=Button(frame,text=1,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(1),
               font=20)
Number2=Button(frame,text=2,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(2),
               font=20)
Number3=Button(frame,
               text=3,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(3),
               font=20)
Number4=Button(frame,
               text=4,
               fg="green",
               height=3,width=3,
               command=lambda:operation(4),
               font=20)
Number5=Button(frame,
               text=5,
               fg="green",
               height=3,width=3,
               command=lambda:operation(5),
               font=20)
Number6=Button(frame,
               text=6,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(6),
               font=20)
Number7=Button(frame,
               text=7,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(7),
               font=20)
Number8=Button(frame,
               text=8,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(8),
               font=20)
Number9=Button(frame,
               text=9,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(9),
               font=20)
Number0=Button(frame,
               text=0,
               fg="green",
               height=3,
               width=3,
               command=lambda:operation(0),
               font=20)
plus=Button(frame,
            text='+',
            fg="green",
            height=3,
            width=3,
            command=lambda:operation('+'),
            font=20)
minus=Button(frame,
             text='-',
             fg="green",
             height=3,
             width=3,
             command=lambda:operation('-'),
             font=20)
multiplication=Button(frame,
                      text='*',
                      fg="green",
                      height=3,
                      width=3,
                      command=lambda:operation('*'),
                      font=20)
division=Button(frame,
                text='/',
                fg="green",
                height=3,
                width=3,
                command=lambda:operation('/'),
                font=20)
equals=Button(window,
              text='=',
              fg="green",
              height=3,
              width=3,
              command=result,
              font=20)
clc=Button(frame,
           text='clc',
           fg="green",
           height=3,
           width=3,
           command=clear,
           font=20)
decimal=Button(frame,
               text='.',
               fg="green",
               height=3,
               width=3,
               command=lambda:operation('.'),
               font=20)

Number1.grid(row=0,column=0)
Number2.grid(row=0,column=1)
Number3.grid(row=0,column=2)
Number4.grid(row=1,column=0)
Number5.grid(row=1,column=1)
Number6.grid(row=1,column=2)
Number7.grid(row=2,column=0)
Number8.grid(row=2,column=1)
Number9.grid(row=2,column=2)
Number0.grid(row=3,column=0)
plus.grid(row=0,column=3)
minus.grid(row=1,column=3)
multiplication.grid(row=2,column=3)
division.grid(row=3,column=3)
clc.grid(row=3,column=2)
decimal.grid(row=3,column=1)
equals.pack()
window.mainloop()

