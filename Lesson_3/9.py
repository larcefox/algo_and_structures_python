# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import choices


def matrix_min_in_col():
    sec = range(-100, 100)
    matrix = [choices(sec, k=5),
              choices(sec, k=5),
              choices(sec, k=5),
              choices(sec, k=5),
              choices(sec, k=5)]
    print(matrix)
    min_in_col = [min(i) for i in [*zip(*matrix)]]
    return max(min_in_col)


print(matrix_min_in_col())
