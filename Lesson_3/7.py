"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
lst = [1, 3, -15, 9, -3, 21, ]

minimum_1st, minimum_2nd = sorted(lst)[:2]

print(minimum_1st, minimum_2nd)