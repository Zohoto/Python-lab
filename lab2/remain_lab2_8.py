day = int(input("Введите день своего рождения: "))
month = int(input("Введите месяц своего рождения: "))
variant = (day + month) % 4
print(variant+1)
