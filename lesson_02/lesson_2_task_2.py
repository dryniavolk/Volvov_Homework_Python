def is_year_leap(number):
    if number % 4 == 0:
        return True
    else:
        return False


year = int(input("Введите год для проверки-"))
result = (is_year_leap(year))
print(f"Год {year}: {result}")
