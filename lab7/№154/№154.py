# Задача №154. НОД

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
print("НОД: %s" % gcd(a, b))
