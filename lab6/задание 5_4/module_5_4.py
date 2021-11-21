def points_circle(s):
    radius = int(s[0])
    square = (2 * radius - 1) ** 2  # используем площадь квадрата, для подсчета
    if radius > 0:
        square += 4
        return (square)
    else:
        return ("Окружности нет")
