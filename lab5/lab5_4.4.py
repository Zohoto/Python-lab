def money(coin):
    rub = coin // 100
    coin = coin % 100
    if rub == 1:
        print(str(rub) + " РУБЛЬ")
    elif (20 >= rub >= 10) or (rub % 10 == "0", "5", "6", "7", "8", "9"):
        print(str(rub) + " РУБЛЕЙ")
    else:
        print(str(rub) + " РУБЛЯ")
    if coin == 1:
        print(str(coin) + " КОПЕЙКА")
    elif 20 >= coin >= 10 or (coin % 10 == "0", "5", "6", "7", "8", "9"):
        print(str(coin) + " КОПЕЕК")
    else:
        print(str(coin) + " КОПЕЙКИ")


coin = int(input())
money(coin)
