""" Генератор простых чиссел"""

import os
from module_5_3 import check_numbers

if os.path.exists("D:\python\pythonProject\lab6\задание 5_3\input6_5_3.txt"):  # проверка существование файла
    file = open("input6_5_3.txt", 'r')
    num = int(file.readline())  # считываем значение
    check_numbers(num)
    file.close()
else:
    file1 = open("output6_5_3.txt", "w")
    file1.write("Файл с входными данными не обнаружен")
    file1.close()
