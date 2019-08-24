

import sys
import time
import Scripts.BlackListOfClients
# Изначальное значение по кредиту "Кредит одобрен".
credit = True

#
def calculate_loan_amount(loan_amount,credit_period):
    ttt= int(loan_amount) / int(credit_period)
    return ttt




# В этой функции мы получаем дополнительный данные о заемщике,и делаем дополнительный анализ.
def Algoritm_Vidahi_Kredita (years):

    sex_borrower = input("Ваш пол (man/woman) ?")
    if sex_borrower == "man":

        # Получаем ответ на вопрос"Какой ежемесячный доход заёмщика".
        monthly_income = int(input("Какой ежемесячный доход заёмщика?"))

        # Получаем ответ на вопрос"У Вас есть военный билет?".
        military_ID = input("У Вас есть военный билет?")
        if  (years > 18 and military_ID == False) and (
                years < 27 and military_ID == False):
            credit = False
            print("Вам отказано в кредите!")
        else:

            # Получает ответ на вопрос "Какую сумму хотите взять в кредит ?".
            loan_amount = input("Какую сумму хотите взять в кредит ?") #Сумма кредита.

            # Поучаем ответ на вопрос.
            credit_period = input("На какой срок хотите взять кредит (Укажите пожалуйста количество месяцев)") # срок кредитования.
            # Расчитываем сумму кредита по параметрам.
            calculate = calculate_loan_amount(loan_amount,credit_period)
            print(calculate)

    elif sex_borrower == "woman":
        pass
    else:
        print("Ошибка")





# Получаем ответ.Фамилию ,Имя,Отчество.
familia_mane_patronymic = input("""Скажите пожалуйста полностью Вашу: Фамилию,Имя,Отчество
Используйте символы 'А-Я,а-я'
Пример : 'Петров Игорь Витальевич'""")
familia_mane_patronymic = familia_mane_patronymic.title()

# Получем даные на вопрос.
series_and_number = input("""Введите серию и номер паспорта
Пример : 2100 668122 """)

# Получаем ответ на вопрос"Дата рождения заемщика(клиента)".
date_of_birth = input("""Введите полностью свою дату рождения
Пример : 01.05.1990 """)
# Проводим вычислительные действия с датой рождения.
# а имено получаем год рождения.
years_date_of_birth = int(date_of_birth[6:])
god = time.localtime()
god = int (god[0])
# Выястняем сколько полных лет заямщику(клиент).
years = god - years_date_of_birth

if years <18 or years >65:
    credit = False
    print("Извените {0} но Вам отказано в кредите!".format(familia_mane_patronymic))

else:
    # Вызываем функцию"Черный список"и в этой функцции анализируем персональные данные.
    blacklist = Scripts.BlackListOfClients.Black_list_of_clients(familia_mane_patronymic,series_and_number,date_of_birth)
    # Если из функции пришел ответ False.
    if blacklist == False:
        print("Извените {0} но Вам отказано в кредите.".format(familia_mane_patronymic))
    else:
        # Если из функции пришел ответ True.
        # Вызоваем функцию для дальнейшего анализа данных.
        Algoritm_Vidahi_Kredita (years)



