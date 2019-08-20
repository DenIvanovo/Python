#Калькулятор V 2.0
#Учимся программированию на Python

def the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с): #Получаем аргументы.

    sum_arguments = eval("("+str(Number_a) + str(Calculator)+ str(Number_b)+")" +str(Further)+ str(Number_с))  #Сумируем все агрументы и получаем сумму.

    return sum_arguments        #Ответ передаем обратно ,откуда была вызвана функция.


Calculator = input("Что будем делать?(+,-,*,/)")

if Calculator == "":
    print("Вы не ввели не одного действия!")

else:

    Number_a = float(input("Введите первое число : "))     #Запрашиваем первое число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
    Number_b = float(input("Введите второе число : "))     #Запрашиваем второе число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.

    if Calculator == "+":

        sum = Number_a + Number_b                         #Получаем сумму чисел.

        print("Результат  :"+ str(Number_a) + " + " +str(Number_b) + " = " + str(sum))   #Сообщаем  результат,через функцию Print()
        Further = input("Ваши дальнейшие дествия ?(+,-,*,/)")  #Ждем дальнейших действий.

        if Further == "+":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " + "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()

        elif Further == "-":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " + "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "*":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " + "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "/":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " + "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        else:
            print("я не понимаю какие действия нужно выполнить!,исправте ошибку.")

    elif Calculator == "-":

        sum = Number_a - Number_b
        print("Результат :"+ str(Number_a) + " - "+str(Number_b) + " = " + str(sum) )     #Сообщаем результат ,через функцию print()

        Further = input("Ваши дальнейшие дествия ?(+,-,*,/)")  #Ждем дальнейших действий.

        if Further == "+":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " - "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()

        elif Further == "-":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " - "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "*":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " - "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "/":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " - "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        else:
            print("я не понимаю какие действия нужно выполнить!,исправте ошибку.")

    elif Calculator == "*":

        sum = Number_a * Number_b
        print("Результат :"+ str(Number_a)+ " * "+ str(Number_b) + " = " + str(sum))   # Сооб5щаем результат,черз функцию print()

        Further = input("Ваши дальнейшие дествия ?(+,-,*,/)")  #Ждем дальнейших действий.

        if Further == "+":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " * "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()

        elif Further == "-":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " * "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "*":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " * "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "/":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " * "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        else:
            print("я не понимаю какие действия нужно выполнить!,исправте ошибку.")

    elif Calculator == "/":

        sum = Number_a / Number_b

        print("Результат :" + str(Number_a) + " / " + str(Number_b)+ " = "+ str(sum))  # Сообщаем результат ,через функцию print()

        Further = input("Ваши дальнейшие дествия ?(+,-,*,/)")  #Ждем дальнейших действий.

        if Further == "+":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " / "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()

        elif Further == "-":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " / "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "*":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " / "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()
        elif Further == "/":

            Number_с = float(input("Введите число !"))                #Запрашиваем  число?Функция Input  свегда возвращает тип стока,и по этому стоку мы ппереводим в число.
            sum_2 = the_sum_of_the_arguments (Number_a,Calculator,Number_b,Further,Number_с)                  #Вычисляем сумму.

            print("Результат  :" + "(" + str(Number_a) + " / "+ str(Number_b)+")" + Further + str( Number_с) + " = "+ str(sum_2))   #Сообщаем  результат,через функцию Print()


        else:
            print("я не понимаю какие действия нужно выполнить!,исправте ошибку.")

    else:
     ####продолжаем писать калькулятор

        print("Чтоттакое я незнаю")




input("Нажмите Enter,чтобы закрыть программу!")
