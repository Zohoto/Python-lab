from math import sqrt

A = float(input("Введите число А: "))
B = float(input("Введите число B: "))
C = float(input("Введите число C: "))


def discriminant():
    D = B ** 2 - 4 * A * C
    return D


def formatting(num):
    print(format(num, ".5f"))


def equation():
    print("Уравнение")
    print("(%.5f)*X^2+(%.5f)*X+(%.5f)=0" % (A, B, C))


# main program
if A == 0:
    print("Число A не может быть равно 0")
else:
    if discriminant() > 0:
        equation()
        x_1 = (-B + sqrt(discriminant())) / (2 * A)
        x_2 = (-B - sqrt(discriminant())) / (2 * A)
        print("Количество корней: 2")
        if x_1 > x_2:
            formatting(x_2)
            formatting(x_1)
        else:
            formatting(x_1)
            formatting(x_2)
    elif discriminant() == 0:
        equation()
        x_1 = (-B + sqrt(discriminant())) / (2 * A)
        x_2 = (-B - sqrt(discriminant())) / (2 * A)
        print("Количество корней: 1")
        formatting(x_1)
        formatting(x_2)
    else:
        equation()
        print("Количесто корней 0")
