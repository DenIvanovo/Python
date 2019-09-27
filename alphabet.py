

alphabet = ("Аа", "Бб", "Вв", "Гг", "Дд", "Ее", "Ёё", "Жж", "Зз", "Ии", "Йй","Кк","Лл","Мм","Нн",
            "Оо","Пп","Рр","Сс","Тт","Уу","Фф","Хх","Цц","Чч","Шш","Щщ","Ъъ","Ыы","Ьь","Ээ","Юю","Яя")

row = 1
ind = 0
while row < 5:
    symbol = 0
    while symbol < 9:
        print("%4s" % (alphabet[ind]), end="")
        if ind == (len(alphabet) - 1):
            break
        ind += 1
        symbol += 1
    print()
    row += 1

