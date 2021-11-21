"""Прямоугольники и квадраты"""

from module_5_1 import PrintRectangle, PrintSquare

file = open('rectangle_input.txt', 'r')
a, b = map(int, file.readline().split())  # считыванием значения сторон прямоугольника
out_Rectangle = file.readline()
PrintRectangle(a, b, out_Rectangle)  # вызовываем функцию
file.close()

file = open('square_input.txt', 'r')
c = int(file.readline())  # считыванием значение стороны квадрата
out_Square = file.readline()
PrintSquare(c, out_Square)  # вызоваем функцию
