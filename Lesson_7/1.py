"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random
import timeit

array = [random.randint(-100, 100) for _ in range(10)]
print(array)


def bubble(array):

    i = 1
    while i < len(array):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

        i += 1
    return print(array)


def bubble_new(array):

    i = 1

    while i < len(array):
        for j in range(len(array) - i):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            if array[-j - 1] < array[-j - 2]:
                array[-j - 1], array[-j - 2] = array[-j - 2], array[-j - 1]

        i += 1
    return print(array)


def bubble_new1(array):

    i = 1

    while i < len(array):
        for j in range(len(array) - i):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            if array[-j - 1] < array[-j - 2]:
                array[-j - 1], array[-j - 2] = array[-j - 2], array[-j - 1]

        for k in range(len(array) - 1):
            if array[k] > array[k + 1]:
                break
        else:
            return print(array)

        i += 1
    return print(array)


def bubble_new2(array):

    i = 1

    while i < len(array):
        for j in range(len(array) - i):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

        for k in range(len(array) - 1):
            if array[k] > array[k + 1]:
                break
        else:
            return print(array)

        i += 1
    return print(array)


if __name__ == '__main__':
  print(timeit.timeit(f'bubble({array})', setup='from __main__ import bubble', number=1), 'Обычный')
  print(timeit.timeit(f'bubble_new({array})', setup= 'from __main__ import bubble_new', number=1), 'Двусторонний')
  print(timeit.timeit(f'bubble_new1({array})', setup='from __main__ import bubble_new1', number=1), 'Двусторонний')
  print(timeit.timeit(f'bubble_new2({array})', setup='from __main__ import bubble_new2', number=1), 'С отсечением')



