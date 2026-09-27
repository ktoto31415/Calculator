from tkinter import *
from tkinter import ttk

window=Tk()
window.title("Калькулятор")
window.geometry('200x200')

countstr=""
x=0
y=0
symbol=""
answer=0

def countstrupdate ():                           #обновить строку ввода в формате    x+y    с учётом неоконченности
    global countstr, countstrotr, x, y, symbol     
    
    if x != 0:
        if symbol != "":
            if y != 0:
                countstr=f"{x}{symbol}{y}"
            else:
                countstr=f"{x}{symbol}"
        else:        
            countstr=f"{x}"
    else:
        countstr = ""

    countstrotr.delete(0, END)
    countstrotr.insert(0,countstr)

def set_with_equality(from_):                 #присвоить содержимое from к переменной symbol
    global symbol
    symbol=from_
    countstrupdate()

    print(from_)                                  #debug
    if symbol != "":                              #debug
        print("symbol=",symbol)                   #debug
    else:                                         #debug
        print("symbol=","NONE")                   #debug

def set_btns_in_square(startx: int, starty: int, shiftx: int, shifty: int, in_row: int, butons):        #отрисовать кнопки в виде квадрата
    for index, i in enumerate (butons):
        i.place(x=startx, y=starty)
        startx+=shiftx 
        if (index+1)%in_row==0:
            startx=40
            
            starty+=shifty 

def set_buton_in_existing_square(startx: int, starty: int, shiftx: int, shifty: int, curentcolumn: int, curentrow: int, btn):   #отрисовать кнопку в формате квадрата из кнопок по координатам 
    btn.place(x=startx+shiftx*(curentcolumn-1), y=starty+shifty*(curentrow-1))



def number(numb):                #поддержка постепенного ввода десятичных цифр и определение цели в соответсвии с наличием знака
    global x, y, symbol
    if x <1000000000 and y <1000000000:
        if symbol == "":
            x = x*10 + numb
            print("x=",x)                   #debug
        else:
            y = y*10 + numb
            print("y=",y)                   #debug
        countstrupdate()

def backspace():
    global x, y, symbol
    if y == 0:
        if symbol == "":
            x=x//10
        else:
            symbol=""
    else:
        y=y//10
    countstrupdate()

def ac():
    global x, y, symbol
    x = 0
    y = 0
    symbol=""
    countstrupdate()

countstrotr=ttk.Entry(text=countstr)                                         #определение элементов окна
btnequality=Button(text="=", command=lambda: calculate())
btnbackspace=Button(text="⌫ ", command=lambda: backspace())
btnac=Button(text="AC", command=lambda: ac())
btnplus=Button(text="+", command=lambda: set_with_equality("+"))
btnminus=Button(text="- ", command=lambda: set_with_equality("-"))
btnumn=Button(text="* ", command=lambda: set_with_equality("*"))
btn1=Button(text=1, command=lambda: number(1))
btn2=Button(text=2, command=lambda: number(2))
btn3=Button(text=3, command=lambda: number(3))
btn4=Button(text=4, command=lambda: number(4))
btn5=Button(text=5, command=lambda: number(5))
btn6=Button(text=6, command=lambda: number(6))
btn7=Button(text=7, command=lambda: number(7))
btn8=Button(text=8, command=lambda: number(8))
btn9=Button(text=9, command=lambda: number(9))
btn0=Button(text=0, command=lambda: number(0))
print(btn0)

butons_in_square_for_number=[btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

countstrotr.place(x=10, y=0)                                                    #отрисовка
set_btns_in_square(40, 20, 20, 30, 3, butons_in_square_for_number)
set_buton_in_existing_square(40, 20, 20, 30, 2, 4, btn0)
set_buton_in_existing_square(40, 20, 20, 30, 4, 1, btnplus)
set_buton_in_existing_square(40, 20, 20, 30, 3, 4, btnequality)
set_buton_in_existing_square(40, 20, 20, 30, 1, 4, btnplus)
set_buton_in_existing_square(40, 20, 20, 30, 4, 2, btnminus)
set_buton_in_existing_square(40, 20, 20, 30, 4, 1, btnumn)
set_buton_in_existing_square(40, 20, 20, 30, 4, 3, btnbackspace)
set_buton_in_existing_square(40, 20, 20, 30, 4, 4, btnac)


window.mainloop()