from tkinter import *
from datetime import *
temp = 0
after_id = ""

def tick():
    global after_id, temp
    # 1000 милисекунд = 1 секунда.
    after_id = root.after(1000,tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    den_root.config(text = str(f_temp))
    temp +=1


def start_command():
    start.grid_forget()  # Прячем кнопку Старт
    stop.grid(row=1,columnspan=2,sticky="ew") # Показываем кнопку Стоп.
    tick()

def stop_command():
    stop.grid_forget()  # Прячем кнопку Стоп.
    reset.grid(row=1,column=0,sticky="ew")  # Показываем кнопку Рестарт.
    restart.grid(row=1,column=1,sticky="ew") # Показываем кнопку Сброс.
    root.after_cancel(after_id)



def reset_command():
    global temp
    temp = 0
    den_root.config(text="00:00", font=("Ubuntu", 100))
    reset.grid_forget()  # Прячем кнопку Рестарт.
    restart.grid_forget()  # Прячем кнопку Сброс.
    start.grid(row=1, columnspan=2, sticky="ew")


def restart_commsnd():
    reset.grid_forget()  # Прячем кнопку Рестарт.
    restart.grid_forget()  # Прячем кнопку Сброс.
    stop.grid(row=1, columnspan=2, sticky="ew")
    tick()


root = Tk()
root.title("Секундомер")
root.geometry("+450+350")

den_root=Label(root,width=5,font=("Ubuntu",100),text="00:00")
den_root.grid(row=0,columnspan=2)

# Создаем кнопки.
start = Button(root,text = "Старт",font=("Ubuntu",30),command=start_command)
stop = Button(root,text = "Стор",font=("Ubuntu",30),command=stop_command )
reset = Button(root,text = "Сбросить",font=("Ubuntu",30),command=reset_command)
restart = Button(root,text = "Рестарт",font=("Ubuntu",30),command=restart_commsnd)

start.grid(row=1,columnspan=2,sticky="ew")

root.mainloop()