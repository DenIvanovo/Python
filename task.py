"""
Создать программу, которая запрашивает числа у пользователя, 
пока тот не введет слово СТОП. Программа должна вывести цифры и их количество, 
используемые при вводе запрашиваемых чисел.
"""

container = []

while True:
     request = input("Введите число :")
     request = request.upper()
     if request == "СТОП":
         break
     else:
         if not request.isdecimal():
             print("Ошибка ввода")
             continue
         else:
             container.append(request)
             continue


transformation = "".join(container)  # Преоброзование "списка" в "строку".
for x in range(0,10):  # Используем диапозон от 0 до 9.
    if str(x) in transformation:  # Проверем на вхождения в строку.
        number = transformation.count(str(x))  # Подсчитывает количество совпадений в строке.
        print("{0} - Количество {1}".format(x,number))




