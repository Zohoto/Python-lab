"""Все о цифрах в числе"""

import os
from module_5_2 import characterization

if os.path.exists('D:\python\pythonProject\lab6\задание 5_2\input6_5_2.txt'):  # проверка существование файла

    file = open('input6_5_2.txt', 'r')
    num = file.readline().split()
    characterization(num)
    file.close()

else:
    f1 = open("output_6_5_2.txt", "w")
    f1.write("Файл с входными данными не обнаружен")
    f1.close()
