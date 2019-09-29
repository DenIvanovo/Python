"""
Програма запрошивает у пользователя числа до тех пор,пока пользователь не введет"СТОП"
После этого выводит числа и их  количество.
"""

container = []

while True:
     request = input("Введите число :")
     if request == "Стоп":
         break
     else:
         if not request.isdecimal():
             print("Ошибка ввода")
             continue
         else:
             request = int(request)
             container.append(request)
             continue

print(container)
print("Количество  " + str(len(container)))
