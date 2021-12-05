# Задача №113652
def function(n):
    if n < 1:
        return "No"
    elif n == 1:
        return "Yes"
    else:
        if function(n - 5) == "Yes":
            return function(n - 5)
        else:
            return function(n - 3)


n = int(input("Введите натурально число, которое не превышает 200: "))
print(function(n))
