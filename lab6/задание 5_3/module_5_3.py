def check_numbers(num):
    file1 = open("output6_5_3.txt", "w")
    for i in range(2, num):  # проверяем простоту чисел
        k = 0
        for j in range(2, (i // 2) + 1):
            if (i % j == 0):
                k = k + 1
        if k == 0:
            file1.write(str(i) + ' ')
    file1.close()