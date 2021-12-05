# Задача №3050 Ханойские башни

def towers(n, stem_start, stem_end):
    if n == 1:
        print(1, stem_start, stem_end)
    else:
        towers(n - 1, stem_start, 6 - stem_start - stem_end)
        print(n, stem_start, stem_end)
        towers(n - 1, 6 - stem_start - stem_end, stem_end)


n = int(input())
towers(n, 1, 3)
