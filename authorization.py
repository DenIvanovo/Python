""""
Контролируем количество попыток введения пароля.
Если ввод более 3 попыток с Неправильным паролем,тогда
блокируем аккаунд на 60 минут.

После каждого Неправильного ввода пароля или логина предупреждаем пользователя и
сообщаем ему сколько попыток осталось.

"""
import socket
import requests
import json
import datetime
# /////////////////////////////////////////////////////////////////////////////////////////////////////
"""
Создаем пустой справочник 'site_user' в нем хроняться логины и пароли зарегистрированных пользователей.
сам справочник мы загруаем из внешнего файла с типом json
Создаем справочник 'locked_ip' для блокированных ip адресов.т.е.(
если пользователь Неправильно вводит 3 раза логин или пароль его ip заноситься в справочник)
инфу в справочники мы получаем из внешнего файла с типом json.
"""
locked_ip = {}
site_users = {}

files_site_user = "site_user.json"
with open(files_site_user, encoding="UTF-8")as f:
    site_users = json.load(f)

ip_file = "ip_file.json"
with open(ip_file) as ip:
    locked_ip = json.load(ip)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
Получаем локальный ip
Осуществляем проверку незаблокирован ли IP пользователя,
перед тем как авторизоваться,если ip есть в справочнике тогда отказ в авторизации)
"""
ip_user = requests.get("https://httpbin.org/ip").json()['origin'].split(',')[0]

while True:
    ip_loc_check = ip_user in locked_ip
    if ip_loc_check:
        rtrtr = locked_ip[ip_user]
        print("Вы заблокированы.Время разблокировки {0}".format(rtrtr))
        break
    else:
        # Иницилизируем попытки.
        attempt = 0

        while attempt < 3:



            user_login = input("Введите логин")
            user_login = user_login.capitalize()
            user_pass = int(input("Введите пароль"))
            # Поиск введеного пользователя в справочнике.

            user_search = user_login in site_users
            if user_search:
                password = site_users[user_login]
                if user_pass == password:
                    print("Авторизация прошла успешна")
                    break
                else:
                    print("Ошибка.Неправильно введен 'пароль'.Осталось {0} попытки(ток)".format((2 - attempt)))
                    attempt += 1
                    continue
            else:
                print("Ошибка.Неправильно введен 'логин'.Осталось {0} попытки(ток)".format((2 - attempt)))
                attempt += 1
                continue

        if attempt == 3:
            print("Вы заблокированы на '1' час.")
            lock_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%d/%m/%y  %X")
            locked_ip[ip_user] = lock_time
            ip_file = "ip_file.json"
            with open(ip_file, "w")as ii:
                json.dump(locked_ip, ii)

        else:
            print(4444)
