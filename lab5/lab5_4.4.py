def money(coin):
    rub = coin // 100
    coin = coin % 100
    if rub > 0:
        if rub % 10 == 1:
            print(str(rub) + " РУБЛЬ")
        elif (10 <= rub <= 20) or (5 <= rub % 10 <= 9) or rub % 10 == 0:
            print(str(rub) + " РУБЛЕЙ")
        else:
            print(str(rub) + " РУБЛЯ")
    if coin > 0:
        if coin % 10 == 1:
            print(str(coin) + " КОПЕЙКА")
        elif (10 <= rub <= 20) or (5 <= rub % 10 <= 9) or rub % 10 == 0:
            print(str(coin) + " КОПЕЕК")
        else:
            print(str(coin) + " КОПЕЙКИ")


coin = int(input("Введите количество копеек: "))
money(coin)
