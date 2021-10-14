a = float(input("Чему равна длина первой стороны? "))
b = float(input("Чему равна длина второй стороны? "))
c = float(input("Чему равна длина третьей стороны? "))


def check():
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False


# check - проверяется, существует ли треугольник

def kind():
    if (a == b) and (b == c):
        return 1
    elif (a == b) or (b == c) or (a == c):
        return 2
    else:
        return 3


# kind - если существует, то какого он вида

if check() == True:
    if kind() == 1:
        print("Треугольник равносторонний")
    elif kind() == 2:
        print("Треугольник равнобедренный")
    elif kind() == 3:
        print("Треугольник общего вида")
else:
    print("Треугольник не существует")
