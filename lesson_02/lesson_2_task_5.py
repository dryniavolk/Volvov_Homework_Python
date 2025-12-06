def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    return "Нет такого месяца,введите верное значение"


month = int(input("Введите искомый месяц от 1 до 12:- "))
print(month_to_season(month))
