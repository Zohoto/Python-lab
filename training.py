import random
list = []
num = 0
while num != 100:
    num_a = random.randint(0,100)
    list.append(num_a)
    num += 1
print(list)
num_sum = 0
num_multi = 1
for i in list:
    num_sum += i
    num_multi *= i
print("сумма: " + str(num_sum), "\n" "произведение: " + str(num_multi))
print("максимум: " + str(max(list)))
list_2 = sorted(list)
print(list_2)
num_num = 1
j = list_2[0]
for j in range(1, len(list_2)):
    if list_2[j] == list_2[j-1]:
        num_num += 1
        if j+1 == max(list_2) and num_num > 1:
            print(str(list_2[j]) + ',', str(num_num))
    elif list_2[j] > list_2[j-1]:
        if num_num > 1:
            print(str(list_2[j-1]) + ',', str(num_num))
        num_num = 1
max = max(list)
min = min(list)
for i in range(len(list)):
    if list[i] == max:
        list[i] = min
    elif list[i] == min:
        list[i] = max
print(list)
