# Задача №3052. Циклические башни
def towers_3(n, start, end):
    if n > 0:
        if (start, end) == (1, 2) or (start, end) == (2, 3) or (start, end) == (3, 1):
            towers_3(n - 1, start, 6 - start - end)
            print(n, start, end)
            towers_3(n - 1, 6 - start - end, end)
        else:
            towers_3(n - 1, start, end)
            print(n, start, 6 - start - end)
            towers_3(n - 1, end, start)
            print(n, 6 - start - end, end)
            towers_3(n - 1, start, end)


n = int(input())
towers_3(n, 1, 3)
