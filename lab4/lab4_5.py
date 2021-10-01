name = {}
surname = {}
patronymic = {}
year = {}
disease = {}
for i in range(5):
    name_0 = input("Введите имя: ")
    name[i+1] = name_0
    surname_0 = input("Введите фамилию: ")
    surname[i + 1] = surname_0
    patronymic_0 = input("Введите отчество: ")
    patronymic[i + 1] = patronymic_0
    year_0 = input("Дата рождения: ")
    year[i + 1] = year_0
    disease_0 = input("Имеете ли болезнь: ")
    disease[i + 1] = disease_0
print("№", "Имя ", "Фамилия", "Отчества", "Дата рождения", "Болезнь")
for j in range(5):
    print(j+1, str(name[j+1]), str(surname[j+1]), str(patronymic[j+1]), str(year[j+1]), str(disease[j+1]))