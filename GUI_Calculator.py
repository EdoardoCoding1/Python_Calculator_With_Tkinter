"""

# Hey there !!

This is my GUI calculator I created by using the tkinter library.

In order to run this program here are the tools you need :

https://www.python.org/downloads/ <-- Download Python

$ brew install python-tk <-- Install tkinter on Mac with homebrew

"""

from tkinter import *

window = Tk()
window.geometry()
window.title('Calculator')
window.iconbitmap(r'\Downloads\Python_Calculator_With_Tkinter\calculator.ico')  #  NOQA

e = Entry(window, width=35, borderwidth=15)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

myLabel = Label(window, text="ED")
myLabel.grid(row=6, column=0)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))


def button_equals():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "power_of":
        e.insert(0, f_num ** float(second_number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        e.delete(0, END)
    except (ZeroDivisionError):
        e.insert(0, 'Error : Cannot Divide By 0')


def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power_of"
    f_num = float(first_number)
    e.delete(0, END)


def button_clear():
    current = e.get()
    e.delete(0, END)

# DEFINE BUTTONS


Button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))  # NOQA
Button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))  # NOQA
Button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))  # NOQA
Button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))  # NOQA
Button_4 = Button(window, text="4", padx=38, pady=20, command=lambda: button_click(4))  # NOQA
Button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))  # NOQA
Button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))  # NOQA
Button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))  # NOQA
Button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))  # NOQA
Button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))  # NOQA


Button_add = Button(window, text="+", padx=17, pady=22, command=button_add)  # NOQA
Button_subtract = Button(window, text="-", padx=40, pady=20, command=button_subtract)  # NOQA
Button_multiply = Button(window, text="X", padx=40, pady=20, command=button_multiply)  # NOQA
Button_divide = Button(window, text="/", padx=40, pady=20, command=button_divide)  # NOQA

Button_equals = Button(window, text="=", padx=17, pady=52, command=button_equals)  # NOQA

Button_clear = Button(window, text="AC", padx=135, pady=20, command=button_clear)  # NOQA
Button_power = Button(window, text="^", padx=18, pady=20, command=button_power)  # NOQA


#  POSITIONS
Button_0.grid(row=4, column=1)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_add.grid(row=1, column=3)
Button_subtract.grid(row=5, column=0)
Button_multiply.grid(row=4, column=2)
Button_divide.grid(row=4, column=0)

Button_equals.grid(row=3, column=3, rowspan=2)
Button_clear.grid(row=5, column=1, columnspan=3)
Button_power.grid(row=2, column=3)

myLabel2 = Label(window, text="PYTHON CALCULATOR")
myLabel2.grid(row=6, column=1, columnspan=3)

window.mainloop()
