"""Матрицы"""

import numpy as np
import random
from module_5_5 import matrix, export

file = open("input6_5_5.txt", "r")  # размеры матрицы А
n = int(file.read(1))
m = int(file.read(2))
file.close()

matrixA = np.random.randint(9, size=(n, m))  # создание матрицы А размером nxm (матрица рандомная, с числами 1...9)

file1 = open("output6_5_5.txt", "w")

file1.write("Матрица A: " + "\n")
for i in matrixA:
    file1.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы А

max_matrixA = np.max(matrixA, axis=1)  # Поиск максимального числа в каждой строке

k = random.randint(5, 15)
matrixB = np.random.randint(9, size=(m, k))  # Создание рандомной матрицы В размером MxK (использую цифры от 1...9)

matrix(m, n, matrixA, max_matrixA)  # Деление всех элементов каждой строки на максимальное число в ней

multi_matrix = matrixA.dot(matrixB)  # Умножение матриц с пмощью numpy

export(matrixA, matrixB, multi_matrix)  # Запись матриц в файл
