import math


def square(side):
    return math.ceil(side ** 2)


side_of_square = float(input("Введите длинну стороны -"))
print(f"Площадь квадрата= {square(side_of_square)}")
