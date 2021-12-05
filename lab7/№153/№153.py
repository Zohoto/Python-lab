# Задача №153. N-е число Фибоначчи
def fib(n):
    if n in range(1, 3):
        return 1
    return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))
