# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python
number = 9
print(type(number))  # Вывод типа переменной number
float_number = 9.0
print(int(float_number))
# Создайте ещё несколько переменных разных типов и осуществите вывод их типов
fact = True
line = "exit"
digit = 5
decimal = 1.5
print("fact -", type(fact))
print("line -", type(line))
print("digit -", type(digit))
print("decimal -", type(decimal))
# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
fact = str(fact)
digit = float(digit)
decimal = int(decimal)
print("fact -", type(fact), "\ndigit -", type(digit), "\ndecimal -", type(decimal))
