def characterization(num):
    n = num[0]
    sum = 0
    multi = 1
    for i in num[0]:
        sum += int(i)  # находим сумму цифр
        multi *= int(i)  # находим произведение цифр

    # выводим необходимые значения в файл
    file = open('output_6_5_2.txt', 'w')
    file.write("Число: " + str(num[0]) + '\n')
    file.write("Количество цифр: " + str(len(n)) + '\n')
    file.write("Сумма: " + str(sum) + '\n')
    file.write("Произведение цифр: " + str(multi))
    file.close()
