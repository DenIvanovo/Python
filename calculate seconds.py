
"""

Программка вычисляет количество лет,месяцев,недель,дней,часов,минут,секунд
из введенного пользователем количества секунд.

"""

seconds = int(input("Введите количество секунд"))
# //// ///// ///////\\\\\\ \\\\\ \\\\
year = seconds // 31536000  # Вычисление количество лет.

year_st = ""
if year == 1:
    year_st = "Год"
elif 2<= year < 5:
    year_st = "Года"
else:
    year_st = "Лет"

residue_second = seconds % 31536000  # Остаток.
# //// ///// ///////\\\\\\\ \\\\\ \\\\
month = residue_second // 2628000  # Вычисляем количество месяцев.

month_st = ""
if month == 1:
    month_st = "Месяц"
elif 2 <= month < 5:
    month_st = "Месяца"
else:
    month_st = "Месяцев"

residue_secon = residue_second % 2628000  # Остаток.
# //// ///// ///////\\\\\\\ \\\\\ \\\\
week = residue_secon // 604800  # Вычисляем количество недель.

week_st = ""
if week == 1:
    week_st = "Неделя"
elif 2 <= week < 5:
    week_st = "Недели"
else:
    week_st = "Недель"

residue_seco = residue_secon % 604800 # Остаток.
# //// ///// ///////\\\\\\\ \\\\\ \\\\
day = residue_seco // 86401  # Вычисляем количество дней.

day_st = ""
if day == 1:
    day_st = "День"
elif 2 <= day < 5:
    day_st = "Дня"
else:
    day_st = "Дней"

residue_sec = residue_seco % 86401  # Остаток.
# //// ///// ///////\\\\\\\ \\\\\ \\\\
clock = residue_sec // 3600  # Высчитываем количество часов.

clock_st = ""
if clock == 1:
    clock_st = "Час"
elif 2 <= clock < 5:
    clock_st = "Часа"
else:
    clock_st = "Часов"

residue_s = residue_sec % 3600  # Остаток.
# //// ///// ///////\\\\\\\ \\\\\ \\\\
minutes = residue_s // 60  # Высчитываем количество минут.

minutes_st = ""
if minutes == 1:
    minutes_st = "Минута"
elif 2<= minutes < 5:
    minutes_st = "Минуты"
else:
    minutes_st = "Мунут"

residue_se = residue_s % 60  # Остаток.

residue_se_st = ""
if residue_se == 1:
    residue_se_st = "Секунда"
elif 2 <= residue_se < 5:
    residue_se_st = "Секунды"
else:
    residue_se_st = "Секунд"


result_ = " {0} {1},{2} {3},{4} {5},{6} {7},{8} {9},{10} {11},{12} {13}".format(year,year_st,month,month_st,week,week_st,day,day_st
                                                            ,clock,clock_st,minutes,minutes_st,residue_se,residue_se_st)

print(result_)


