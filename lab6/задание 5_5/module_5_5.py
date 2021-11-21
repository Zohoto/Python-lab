def matrix(m, n, matrixA, max_matrixA):
    for i in range(n):
        for j in range(m):
            matrixA[i][j] = matrixA[i][j] // max_matrixA[i]  # Деление каждого элемента матрицы на максимальное число

    return matrixA


def export(matrixA, matrixB, multi_matrix):
    file1 = open("output6_5_5.txt", "w")

    file1.write("Матрица A: " + "\n")
    for i in matrixA:
        file1.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы А

    file1.write("Матрица A, деленная на максимальное число в каждой строке: " + "\n")
    for i in matrixA:
        file1.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы А, которую поделили на максимальное число в каждой строке

    file1.write("Матрица B: " + "\n")
    for i in matrixB:
        file1.write(" ".join(map(str, i)) + "\n")  # Вывод матрицы В

    file1.write("Матрица A*B: " + "\n")
    for i in multi_matrix:
        file1.write(" ".join(map(str, i)) + "\n")  # Вывод умножения матрицы А на матрицу В
    file1.close()
