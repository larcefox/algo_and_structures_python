"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple, defaultdict


try:
    corp_count = int(input('Enter number:\n'))
except ValueError:
    print("Data is incorrect!")


corps = namedtuple('Corps', 'name q1 q2 q3 q4')
corp_data = []


for i in range(corp_count):
    try:
        corp_name = input('Enter corporation name:\n')
        corp_data.append(corps(corp_name,
                               q1=int(input('Enter pure income for 1 quarter:\n')),
                               q2=int(input('Enter pure income for 2 quarter:\n')),
                               q3=int(input('Enter pure income for 3 quarter:\n')),
                               q4=int(input('Enter pure income for 4 quarter:\n'))
                               ))
    except ValueError:
        print("Data is incorrect!")
        exit(1)

corp_aver_income = 0

for value in corp_data:
    corp_aver_income += value.q1 + value.q2 + value.q3 + value.q4
else:
    corp_aver_income /= len(corp_data)

for value in corp_data:
    print(f'Income of {value.name} corporation higher or equally average income') \
        if value.q1 + value.q2 + value.q3 + value.q4 >= corp_aver_income else \
        print(f'Income of {value.name} corporation lower then average income')


print(corp_aver_income)

#-----------------------------------------------------------------------------------------------------------------------

d = defaultdict(list)
sort_list = []

for i in range(corp_count):
    corp_name = input('Enter corporation name:\n')

    try:
        [d[corp_name].append(int(input(f'Enter pure income for {j + 1} quarter:\n'))) for j in range(4)]
    except ValueError:
        print("Data is incorrect!")
        exit(1)
    d[corp_name].append(sum(d[corp_name]))


avg_income = sum([k[4] for k in list(d.values())]) / corp_count

print(f'Income of {list(filter(lambda x: d[x][4] > avg_income, d))} corporations is higher than average income')
print(f'Income of {list(filter(lambda x: d[x][4] < avg_income, d))} corporations is lower than average income')
print(f'Income of {list(filter(lambda x: d[x][4] == avg_income, d))} corporations is equal than average income')
