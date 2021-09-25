from random import choice

name = str(input("Введите имя: "))
surname = str(input("Введите фамилию: "))
group = int(input("С какой вы группы? "))
print("Привет, " + surname, name + " из группы " + str(group) + "!")
mail = input("Введи свою электронную почту? ")
name_list = []
for i in range(len(name)):
    name_list.append(name[i])
surname_list = []
for j in range(len(surname)):
    surname_list.append(surname[j])
mail_list = []
for i in range(len(mail)):
    mail_list.append(mail[i])
for j in range(5):
    print(choice(surname_list).lower(), end='')
for j in range(10):
    print(choice(name_list).lower(), end='')
for j in range(15):
    print(choice(mail_list).lower(), end='')
