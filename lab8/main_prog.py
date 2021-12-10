import timeit
from prettytable import PrettyTable
from random import randint
import sorts


def timer(list):  # функция, котороя считает время выполнения различных сортировок
    start = timeit.default_timer()
    sorts.bubble(list)
    b = str((timeit.default_timer() - start))

    start = timeit.default_timer()
    sorts.insertion(list)
    ins = str((timeit.default_timer() - start))

    start = timeit.default_timer()
    sorts.quick(list)
    fast = str((timeit.default_timer() - start))

    list_2 = list.copy()
    start = timeit.default_timer()
    list_2.sort()
    standart = str((timeit.default_timer() - start))
    return b, ins, fast, standart



N = int(input("Введите число элементов последовательностей: "))
list = []  # создание последовательности
for i in range(N):
    list.append(randint(-100000, 100000))
b, ins, fast, standart = timer(list)  # случайная
list.sort()
b2, ins_2, fast_2, standart_2 = timer(list)  # отсортированная
list.reverse()
b3, ins_3, fast_3, standart_3 = timer(list)  # отсортированная в обратном порядке

# таблица
table = PrettyTable()
table.add_column("Метод", ["Метод пузырька", "Сортировка простыми вставками", "Быстрая сортировка", "Встроенная функция"])
table.add_column("Случайная", [b, ins, fast, standart])
table.add_column("Отсортированная", [b2, ins_2, fast_2, standart_2])
table.add_column("Отсортированная в обратном порядке", [b3, ins_3, fast_3, standart_3])

# переносим таблицу в файл
file = open("output.txt", "w")
file.write("Число элементов последовательностей: " + str(N) + '\n')
file.write(str(table))
file.close()
