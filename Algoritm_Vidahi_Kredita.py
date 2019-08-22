
import sys
import time
import Scripts.BlackListOfClients
#Изначальное значение по кредиту "Кредит одобрен"
credit = True


#В этой функции мы получаем дополнительный данные о заемщике,и делаем дополнительный анализ.
def Algoritm_Vidahi_Kredita (familia_mane_patronymic,series_and_number,date_of_birth):
    print("Ваш пол (man/woman) ? ")
    #Получаем ответ на вопрос"Ваш пол".
    sex_borrower = input()
    if sex_borrower == "man":
        print("Какой ежемесячный доход заёмщика?")
        #Получаем ответ на вопрос"Какой ежемесячный доход заёмщика".
        monthly_income = int(input())
        print("У Вас есть военный билет?")
        #Получаем ответ на вопрос"У Вас есть военный билет?".
        military_ID = input()
        if  (the_age_of_the_borrower > 18 and military_ID == False) and (
                the_age_of_the_borrower < 27 and military_ID == False):
            credit = False
            print("Вам отказано в кредите!")
        else:
            print("Какую сумму хотите взять в кредит ?")
            #Получает ответ на вопрос "Какую сумму хотите взять в кредит ?"
            loan_amount = int(input()) #Сумма кредита
            print("На какой срок хотите взять кредит (Укажите пожалуйста количество месяцев)")
            #Поучаем ответ на вопрос.
            credit_period = int(input()) # срок кредитования





#Спрашиваем у заемщика(клиента)Фамилию ,Имя,Отчество
print("""Скажите пожалуйста полностью Вашу: Фамилию,Имя,Отчество
Используйте символы 'А-Я,а-я'
Пример : 'Петров Игорь Витальевич'""")
#Получаем ответ.Фамилию ,Имя,Отчество
familia_mane_patronymic = input()
familia_mane_patronymic = familia_mane_patronymic.title()
#Спрашиваем у заемщика(клиента)Серию и номер паспорта
print("""Введите серию и номер паспорта
Пример : 2100 668122 """)
#Получем даные на вопрос
series_and_number = input()
#Задаем вопрос "Дата рождения заемщика(клиента)".
print("""Введите полностью свою дату рождения
Пример : 01.05.1990 """)
#Получаем ответ на вопрос"Дата рождения заемщика(клиента)".
date_of_birth = input()
#Проводим вычислительные действия с датой рождения
# а имено получаем год рождения
years_date_of_birth = int(date_of_birth[6:])
god = time.localtime()
god = int (god[0])
#Выястняем сколько полных лет заямщику(клиент).
years = god - years_date_of_birth

if years <18 or years >65:
    credit = False
    print("Извените {0} но Вам отказано в кредите!".format(familia_mane_patronymic))

else:
    #Вызываем функцию"Черный список"и в этой функцции анализируем персональные данные
    blacklist = Scripts.BlackListOfClients.Black_list_of_clients(familia_mane_patronymic,series_and_number,date_of_birth)
    #Если из функции пришел ответ False
    if blacklist == False:
        print("Извените {0} но Вам отказано в кредите.".format(familia_mane_patronymic))
    else:
        #Если из функции пришел ответ True
        #Вызоваем функцию для дальнейшего анализа данных
        Algoritm_Vidahi_Kredita (familia_mane_patronymic,series_and_number,date_of_birth)



