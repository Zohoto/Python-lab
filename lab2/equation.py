# 1
from math import sqrt, e
x = float(input("Введите число: "))
if x >= 1 or x <= -1:
    print("Нет решения")
else:
    print("y = " + str(1/sqrt(1 - (x ** 4) - (x ** 2))))

# 2
x = float(input("Введите число: "))
if x < 0:
    print("Нет решения")
else:
    print("y = " + str(e**(sqrt(x+sqrt(x)))))

# 3
x = float(input("Введите число: "))
if x == -1 or x == 1:
    print("Нет решения")
else:
    print("y = " + str(((x**2 + 1) / (3 * (x**2 - 1))) + (x**2 - 1) * (1 - x)))

# 4
x = float(input("Введите число: "))
if x < 0:
    print("Нет решения")
else:
    print("y = " + str(sqrt(x + sqrt(x + sqrt(x)))))
