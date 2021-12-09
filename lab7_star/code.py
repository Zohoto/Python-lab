def board(matrix):  # создаем таблицу, похожую на шахматную доску
    line = len(matrix)
    element = len(matrix[0])
    output = ""
    for i in range(line):
        output += ("{:<4} " * element).format(*matrix[i]) + "\n"
    return output


def accept(x_2, y_2):  # Доступные пути из точки x, y
    motion = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]  # возможные ходы шахматного коня
    possible = []
    for m in motion:
        if (0 <= x_2 + m[0] < N) and (0 <= y_2 + m[1] < M) and (chess[y_2 + m[1]][x_2 + m[0]]) == 0:
            possible.append(m)
    return possible


# правило Варнсдорфа
# Во время обхода доски конь должен идти в то поле, из которого существует минимальное число ходов
def decision():
    x_2 = X - 1
    y_2 = Y - 1
    for i in range(1, M * N + 1):
        chess[y_2][x_2] = i
        next_moves = []
        least = 9
        for move in accept(x_2, y_2):
            count = len(accept(x_2 + move[0], y_2 + move[1]))
            if count < least and (count != 0 or i == N * M - 1):
                least = count
                next_moves = move
        if len(next_moves) == 0:
            break
        x_2 = x_2 + next_moves[0]
        y_2 = y_2 + next_moves[1]
    if i != M * N:
        print("Маршрут не определен. Остановлен на x: %s, y: %s. i = %s}" % (x_2, y_2, i))

# основная программа
file = open("input.txt", "r")
s = file.read().split()
M = int(s[0])
N = int(s[1])  # M и N являются размерами доски
X = int(s[2])
Y = int(s[3])  # X и Y начальная позиция коня
file.close()

chess = [[0 for j in range(N)] for i in range(M)]  # создаем примерный макет доски
decision()
print(board(chess))

