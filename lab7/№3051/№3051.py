# Задача №3051. Ремонт в Ханое
def towers_2(n, start, end):
    if n > 0:
        if (6 - start - end) == 2:
            towers_2(n - 1, start, end)
            print(n, start, 6 - start - end)
            towers_2(n - 1, end, start)
            print(n, 6 - start - end, end)
            towers_2(n - 1, start, end)
        else:
            towers_2(n - 1, start, 6 - start - end)
            print(n, start, end)
            towers_2(n - 1, 6 - start - end, end)


n = int(input())
towers_2(n, 1, 3)
