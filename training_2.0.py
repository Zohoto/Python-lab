month = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
         7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

year_16 = {1: '22000', 2: '190000', 3: '245000', 4: '151000', 5: '98000', 6: '354000',
           7: '126000', 8: '124000', 9: '121000', 10: '148237', 11: '252300', 12: '324774'}
max_16 = 0
min_16 = 9999999999
for i in range(1, 13):
    if max_16 < int(year_16[i]):
        max_16 = int(year_16[i])
        max_num_16 = i
    if min_16 > int(year_16[i]):
        min_16 = int(year_16[i])
        min_num_16 = i
print(2016)
print("Пик продаж: " + str(month[max_num_16]), max_16)
print("Минимальные продажи: " + str(month[min_num_16]), min_16)

year_17 = {1: '88000', 2: '168446', 3: '137590', 4: '81000', 5: '102000', 6: '321000',
           7: '345120', 8: '153010', 9: '320172', 10: '231423', 11: '245100', 12: '256484'}
max_17 = 0
min_17 = 9999999999
for i in range(1, 13):
    if max_17 < int(year_17[i]):
        max_17 = int(year_17[i])
        max_num_17 = i
    if min_17 > int(year_17[i]):
        min_17 = int(year_17[i])
        min_num_17 = i
print("\n2017")
print("Пик продаж: " + str(month[max_num_17]), max_17)
print("Минимальные продажи: " + str(month[min_num_17]), min_17)

year_18 = {1: '465000', 2: '285333', 3: '134000', 4: '353000', 5: '136000', 6: '234126',
           7: '345600', 8: '352023', 9: '153230', 10: '172000', 11: '412986', 12: '354128'}
max_18 = 0
min_18 = 9999999999
for i in range(1, 13):
    if max_18 < int(year_18[i]):
        max_18 = int(year_18[i])
        max_num_18 = i
    if min_18 > int(year_18[i]):
        min_18 = int(year_18[i])
        min_num_18 = i
print("\n2018")
print("Пик продаж: " + str(month[max_num_18]), max_18)
print("Минимальные продажи: " + str(month[min_num_18]), min_18)

# years = [year_16, year_17, year_18]
# month_2 = []
# for j in years:
#    for k in range(2, 12):
#        if int(year_16[k]) > int(year_16[k - 1]):
#            month_2.append(month[k - 1])
#        else:
#            if len(month_2) > 1:
#                month_2.append(month[k - 1])
#                print(month_2)
#                month_2 = []
