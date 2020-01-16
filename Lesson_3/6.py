"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

lst = [31, 3, -15, 9, -3, 21, ]

minimum = lst.index(min(lst))
maximum = lst.index(max(lst))

print(sum(lst[minimum + 1:maximum]) if minimum < maximum else sum(lst[maximum + 1:minimum]))

