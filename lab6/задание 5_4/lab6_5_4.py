import os
from datetime import datetime
import time
from module_5_4 import points_circle

if os.path.exists("D:\python\pythonProject\lab6\задание 5_4\input6_5_4.txt"):
    file = open("input6_5_4.txt", "r")
    s = file.read().split()
    file.close()

    file1 = open("output6_5_4.txt", "w")
    file1.write(str(datetime.now()))  # Вывод текущего времени

    periods = points_circle(s)  # вызов модуля для подсчета точек
    file1.write("\n" + str(periods))

    runtime = time.process_time()
    file1.write("\n" + str(runtime))  # Вывод времени выполнения программы

    file1.close()
else:
    file1 = open("output6_5_4.txt", "w")
    file1.write("Файл с входными данными не обнаружен")
    file1.close()
