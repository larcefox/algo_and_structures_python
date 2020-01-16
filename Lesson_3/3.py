#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

lst = [1, 3, 15, 8, 2, 7, ]

lst_copy = lst
lst_copy[lst.index(max(lst))], lst_copy[lst.index(min(lst))] = min(lst), max(lst)
lst = lst_copy

print(lst)
