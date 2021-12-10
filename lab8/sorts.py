from random import choice

# 1 Обменная сортировка (метод пузырька)
def bubble(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                cushion = list[j]
                list[j] = list[j+1]
                list[j+1] = cushion
    return list


# 2 Сортировка простыми вставками;
def insertion(list):
    for pos in range(len(list)):
        point = list[pos]
        while pos > 0 and list[pos - 1] > point:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = point

    return list

# 6 Быстрая сортировка
def quick(list):
    if len(list) <= 1:
        return list
    else:
        q = choice(list)
        num_s = []
        num_m = []
        num_e = []
        for n in list:
            if n < q:
                num_s.append(n)
            elif n > q:
                num_m.append(n)
            else:
                num_e.append(n)
        return quick(num_s) + num_e + quick(num_m)

def check(list):
    for k in range(1, len(list)):
        if list[k-1] > list[k]:
            return False
        return True
