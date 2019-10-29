#Калькулятор V 2.0
#Учимся программированию на Python

from tkinter import *

user_input = ""
def quantity(value):
    global user_input
    if value == "=":
        user_input = str(eval(user_input))
        monitor.config(text=user_input)
        user_input = ""
    elif value == "gray":
        user_input = user_input[:-1]
        monitor.config(text=user_input)
    else:
        user_input = user_input + value
        monitor.config(text=user_input)

root = Tk()
root.title("Калькулятор")
root.geometry("550x350+400+350")

monitor = Label(root,text= 0,font = ("Ubuntu",40))
monitor.grid(row=0,columnspan=3,sticky="e")

# Создаем кнопки для калькулятора.
button_1 = Button(root,text="1",font = ("Ubuntu",20),width=8,command = lambda: quantity('1'))
button_2 = Button(root,text="2",font = ("Ubuntu",20),width=8,command = lambda: quantity('2'))
button_3 = Button(root,text="3",font = ("Ubuntu",20),width=8,command = lambda: quantity('3'))
button_q = Button(root,text="+",font = ("Ubuntu",20),bg="yellow",width=8,command = lambda: quantity('+'))

button_4 = Button(root,text="4",font = ("Ubuntu",20),width=8,command = lambda: quantity('4'))
button_5 = Button(root,text="5",font = ("Ubuntu",20),width=8,command = lambda: quantity('5'))
button_6 = Button(root,text="6",font = ("Ubuntu",20),width=8,command = lambda: quantity('6'))
button_w = Button(root,text="-",font = ("Ubuntu",20),bg="yellow",width=8,command = lambda: quantity('-'))

button_7 = Button(root,text="7",font = ("Ubuntu",20),width=8,command = lambda: quantity('7'))
button_8 = Button(root,text="8",font = ("Ubuntu",20),width=8,command = lambda: quantity('8'))
button_9 = Button(root,text="9",font = ("Ubuntu",20),width=8,command = lambda: quantity('9'))
button_0 = Button(root,text="0",font = ("Ubuntu",20),width=17,command = lambda: quantity('0'))

button_point = Button(root,text=".",font = ("Ubuntu",20),width=8,command = lambda: quantity('.'))
button_share = Button(root,text="/",font = ("Ubuntu",20),bg="yellow",width=8,command = lambda: quantity('/'))
button_multiply = Button(root,text="*",font = ("Ubuntu",20),bg="yellow",width=8,command = lambda: quantity('*'))
button_calculate = Button(root,text="=",font = ("Ubuntu",20),bg="yellow",width=8,command = lambda: quantity('='))
button_percent = Button(root,text="%",font = ("Ubuntu",20),width=8,command = lambda: quantity('%'))
button_brackets = Button(root,text="(",font = ("Ubuntu",20),width=8,command = lambda: quantity('('))
button_brackets_ = Button(root,text=")",font = ("Ubuntu",20),width=8,command = lambda: quantity(")"))
button_Backspace = Button(root,text="back",font = ("Ubuntu",20)
                          ,bg="gray",width=8,command = lambda: quantity("gray"))

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_q.grid(row=4,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_w.grid(row=3,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,columnspan=2)

button_calculate.grid(row=5,column=3)
button_multiply.grid(row=2,column=3)
button_point.grid(row=5,column=2)
button_share.grid(row=1,column=3)
button_percent.grid(row=1,column=2)
button_brackets.grid(row=1,column=0)
button_brackets_.grid(row=1,column=1)
button_Backspace.grid(row=0,column=3)



root.mainloop()
