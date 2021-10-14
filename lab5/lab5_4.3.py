def time():
    minute = (Motp + Mp)
    hour = ((Hotp + Hp) + minute // 60) % 24
    day = ((Hotp + Hp) + minute // 60) // 24
    minute = minute % 60
    if minute < 10:
        if hour < 10:
            print("0" + str(hour) + " hours :", "0" + str(minute) + " minutes")
            print(str(day) + " days")
            return
        print(str(hour) + " hours :", "0" + str(minute) + " minutes")
        print(str(day) + " days")
        return
    elif hour < 10:
        print("0" + str(hour) + " hours :", str(minute) + " minutes")
        print(str(day) + " days")
        return
    print(str(hour) + " hours :", str(minute) + " minutes")
    print(str(day) + " days")


# main program
Hotp = int(input("Часы отправления: "))  # час отпраления
Motp = int(input("Минуты отправления: "))  # минуты отправления
Hp = int(input("Количество часов в пути: "))  # количество часов в пути
Mp = int(input("Количество минут в пути: "))  # количество минут в пути
HinDAY = 24 # сколько часов в 1 дне
MinDAY = 60 # сколько минут в часе

time()
