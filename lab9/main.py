from random import randint
import timeit
from math import ceil
import sorts

N = 50000  # Количество чисел
M = 60  # Максимальное количество чисел, которые мы можем использовать за раз
P = 4  # Количество файлов, которые мы будем использовать

# Создаем список и заполняем им файл. В каждой строчке находится 60(M) чисел
list_1 = []
for i in range(N):
    list_1.append(randint(-100, 100))

f = open("input.txt", 'w')
for i in range(N // M):
    f.write(" ".join(map(str, list_1[i * M:i * M + M])) + "\n")
f.close()

# Очищаем память
del list_1

# main

start = timeit.default_timer()

tapes = list(sorts.Tape(f"files_6/{i}.txt", 'w') for i in range(P)) # делаем список из лент


# Заполняем первые две ленты нашим списком
f = open("input.txt", 'r')
for i in range(ceil(N / M)):
    list_2 = list(map(int, f.readline().split()))
    sorts.bubble(list_2)  # Сортируем каждый набор пузырьковым методом сортировки
    tapes[i % 2].write(" ".join(map(str, list_2)) + " \n")
f.close()

# mode нужен для смены пары лент
# 0 -  0 и 1 лента
# 1 -  2 и 3 лента
mode = 0
sorts.reopen(tapes, mode)

while True:
    iter1 = tapes[mode * 2].read()
    iter2 = tapes[mode * 2 + 1].read()
    if (not iter1) or (not iter2):  # Проверка файлов на пустоту. Если пустой, то значит массив отсортирован отсортирован
        time = str((timeit.default_timer() - start))
        if iter1:
            print("Отсортирован в " + str(tapes[mode * 2].path))
        else:
            print("Отсортирован " + str(tapes[mode * 2 + 1].path))
        print("Время сортировки: " + str(time))
        break
    num = ((mode + 1) % 2) * 2

    while iter1 or iter2:
        if iter1 == '':
            while iter2 != True:
                if iter2 == "\n":
                    iter2 = tapes[mode * 2 + 1].read()
                    continue
                tapes[num].write(iter2 + ' ')
                iter2 = tapes[mode * 2 + 1].read()
            break
        elif iter2 == '':
            while iter1:
                if iter1 == "\n":
                    iter1 = tapes[mode * 2].read()
                    continue
                tapes[num].write(iter1 + ' ')
                iter1 = tapes[mode * 2].read()
            break

        while iter1 != "\n" or iter2 != "\n":
            if not iter1 or not iter2: # Если какая-нибудь из лент закончилась, мы выходим из цикла
                break
            if iter1 == "\n":
                tapes[num].write(iter2 + " ")
                iter2 = tapes[mode * 2 + 1].read()
                continue
            elif iter2 == "\n":
                tapes[num].write(iter1 + " ")
                iter1 = tapes[mode * 2].read()
                continue
            if int(iter1) < int(iter2):
                tapes[num].write(iter1 + " ")
                iter1 = tapes[mode * 2].read()
            else:
                tapes[num].write(iter2 + " ")
                iter2 = tapes[mode * 2 + 1].read()
        if bool(iter1) != bool(iter2):
            continue
        tapes[num].write("\n")
        num = ((mode + 1) % 2) * 2 + (num + 1) % 2  # переключаемся на следующую ленту
        iter1 = tapes[mode * 2].read()
        iter2 = tapes[mode * 2 + 1].read()
    mode = (mode + 1) % 2  # Переключаем режим
    sorts.reopen(tapes, mode)  # Отматываем ленты в самое начало