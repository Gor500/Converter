import tkinter as tk
from tkinter import LEFT, RIGHT, Button, PhotoImage
import tkinter.messagebox as msg

win = tk.Tk()
win.title("Converter")
win.geometry("400x400")

bg = PhotoImage(file="/home/mkhitar/Desktop/blue.png")
label = tk.Label(image=bg)
label.place(x=0,y=0)

tk.Label(text="Converter",font=("Helvetica 20 bold"),fg="Cyan",bg="#00008b").pack(pady=10)

#Decimal
def press_key(str):
    if str.char == "\r":
        decimal_to_binary()
        decimal_to_octal()
        decimal_to_hexdecimal()
    elif str.char == "\x08":
        Binary.delete(0,tk.END)
        Octal.delete(0,tk.END)
        Hexadecimal.delete(0,tk.END)
#Binary
def press_key2(str2):
    try:
        if str2.char == "\r":
            binary_to_decimal()
            binary_to_octal()
            binary_to_hexdecimal()
        elif str2.char == "\x08":
            Decimal.delete(0,tk.END)
            Octal.delete(0,tk.END)
            Hexadecimal.delete(0,tk.END)
    except:
        Decimal.delete(0,tk.END)
        Octal.delete(0,tk.END)
        Hexadecimal.delete(0,tk.END)
        Binary.delete(0,tk.END)
        msg.showerror("Error","You can write only 0 and 1")
#Octal
def press_key3(str3):
    if str3.char == "\r":
        octal_to_binary()
        octal_to_decimal()
        octal_to_hexadecimal()
    elif str3.char == "\x08":
        Binary.delete(0,tk.END)
        Decimal.delete(0,tk.END)
        Hexadecimal.delete(0,tk.END)

def press_key4(str4):
    if str4.char == "\r":
        hexadecimal_to_binary()
        hexadecimal_to_decimal()
        hexadecimal_to_octal()
    elif str4.char == "\x08":
        Binary.delete(0,tk.END)
        Octal.delete(0,tk.END)
        Decimal.delete(0,tk.END)


def decimal_to_binary():
    value = Decimal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Binary.delete(0,tk.END)
    binar = bin(int(value,10))
    Binary.delete(0,tk.END)
    Binary.insert(0,binar[2::])

def binary_to_decimal():
    value = Binary.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Decimal.delete(0,tk.END)
    elif "1" and "0" not in value:
        msg.showinfo("Warning!","You can write only 0 and 1")
        Decimal.delete(0,tk.END)
        Binary.delete(0,tk.END)
    a = int(value)
    decimal = 0
    for digit in str(a):
        decimal = decimal*2 + int(digit)
    Decimal.delete(0,tk.END)
    Decimal.insert(0,decimal)

def decimal_to_octal():
    value = Decimal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Octal.delete(0,tk.END)
    a = int(value)
    octal = oct(a)
    Octal.delete(0,tk.END)
    Octal.insert(0,octal[2::])

def binary_to_octal():
    value = Binary.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Octal.delete(0,tk.END)
    octal_bin = int(value,2)
    octal_bin = oct(octal_bin)
    Octal.delete(0,tk.END)
    Octal.insert(0,octal_bin[2::])

def binary_to_hexdecimal():
    value = Binary.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Hexadecimal.delete(0,tk.END)
    hexdes = hex(int(value,2))
    Hexadecimal.delete(0,tk.END)
    Hexadecimal.insert(0,hexdes[2::])

def decimal_to_hexdecimal():
    value = Decimal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Hexadecimal.delete(0,tk.END)
    hexdes = hex(int(value,10))
    Hexadecimal.delete(0,tk.END)
    Hexadecimal.insert(0,hexdes[2::])
    
def octal_to_binary():
    value = Octal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Binary.delete(0,tk.END)
    octal = bin(int(value,8))
    Binary.delete(0,tk.END)
    Binary.insert(0,octal[2::])

def octal_to_decimal():
    value = Octal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Decimal.delete(0,tk.END)
    decimal = 0
    for digit in value:
     	decimal = decimal*8 + int(digit)
    Decimal.delete(0,tk.END)
    Decimal.insert(0,decimal)

def octal_to_hexadecimal():
    value = Octal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Hexadecimal.delete(0,tk.END)
    hexa = hex(int(value,8))
    Hexadecimal.delete(0,tk.END)
    Hexadecimal.insert(0,hexa[2::])

def hexadecimal_to_binary():
    value = Hexadecimal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Binary.delete(0,tk.END)
    hexa = bin(int(value,16))
    Binary.delete(0,tk.END)
    Binary.insert(0,hexa[2::])

def hexadecimal_to_octal():
    value = Hexadecimal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Octal.delete(0,tk.END)
    octal = int(value,16)
    octal = oct(octal)
    Octal.delete(0,tk.END)
    Octal.insert(0,octal[2::])

def hexadecimal_to_decimal():
    value = Hexadecimal.get()
    if value == "":
        msg.showinfo("Warning: ","Please write a number.")
        Decimal.delete(0,tk.END)
    hexa = int(value,16)
    Decimal.delete(0,tk.END)
    Decimal.insert(0,hexa)


#Binary

frame1 = tk.Frame(win)
tk.Label(frame1, text = "Binary: ", font = ("Helvetica 15 bold"),fg="Cyan",bg="#00008b").pack(side=LEFT)
Binary = tk.Entry(frame1,font=("Helvetica 14 bold"),fg="Cyan",bg="#00008b",highlightthickness=2,highlightbackground="#00008b",highlightcolor="#00008b",width=30)
Binary.pack(side=RIGHT)
frame1.pack(pady=10)
Binary.bind('<Key>', press_key2)


#Decimal

frame2 = tk.Frame(win)
tk.Label(frame2, text = "Decimal: ", font = ("Helvetica 15 bold"),fg="Cyan",bg="#00008b").pack(side=LEFT)
Decimal = tk.Entry(frame2,font=("Helvetica 14 bold"),fg="Cyan",bg="#00008b",highlightthickness=2,highlightbackground="#00008b",highlightcolor="#00008b",width=29)
Decimal.pack(side=RIGHT)
frame2.pack(pady=10)
Decimal.bind('<Key>', press_key)

#Octal

frame3 = tk.Frame(win)
tk.Label(frame3, text = "Octal: ", font = ("Helvetica 15 bold"),fg="Cyan",bg="#00008b").pack(side=LEFT)
Octal = tk.Entry(frame3,font=("Helvetica 14 bold"),fg="Cyan",bg="#00008b",highlightthickness=2,highlightbackground="#00008b",highlightcolor="#00008b",width=31)
Octal.pack(side=RIGHT)
frame3.pack(pady=10)
Octal.bind('<Key>',press_key3)

#HexaDecimal

frame4 = tk.Frame(win)
tk.Label(frame4, text = "Hex: ", font = ("Helvetica 15 bold"),fg="Cyan",bg="#00008b").pack(side=LEFT)
Hexadecimal = tk.Entry(frame4,font=("Helvetica 14 bold"),fg="Cyan",bg="#00008b",highlightthickness=2,highlightbackground="#00008b",highlightcolor="#00008b",width=33)
Hexadecimal.pack(side=RIGHT)
frame4.pack(pady=10)
Hexadecimal.bind('<Key>', press_key4)

def conv():
    decimal_to_octal()
    decimal_to_binary()
    decimal_to_hexdecimal()


Button(text="Convert",font=("Helvetica 15 bold"),command=conv,bg="#00008b",fg="Cyan",highlightbackground="#00008b",highlightthickness=2,highlightcolor="#00008b").pack(pady=10)

win.mainloop()