"""
функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
которая должна быть произведена над ними.
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
"""
def arithmetic(number_a,number_b,argument):

    l_argument = ["+","-","*","/"]
    entry = argument in l_argument
    if entry == True:
        print(eval(number_a + argument + number_b))
    else:
        print("Неизвестная операция!")


number_a = input("Введите первое число:")

while True:
    if not number_a.isdigit():
        print("Ошибка ввода")
        print("Используйте только целые числа.")
        number_a = input("Введите первое число:")
        continue
    else:
        break
number_b = input("Введите второе число:")

while True:
    if not number_b.isdigit():
        print("Ошибка ввода")
        print("Используйте только целые числа.")
        number_b = input("Введите второе число:")
        continue
    else:
        break

argument = input("Введите операцию(+,-,*,/)")

arithmetic(number_a,number_b,argument)

