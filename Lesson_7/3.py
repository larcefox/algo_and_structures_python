"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random
import timeit
from statistics import median

try:
    NUM = int(input('Enter number:\n'))
except ValueError:
    print("Data is not correct")
    exit(1)

array = [random.randint(0, 15) for _ in range(NUM * 2 + 1)]


def median_0(array):
    return median(array)


def median_1(array):
    for i in range(int(len(array) / 2 + 1)):
        array.append(array.pop(array.index(min(array[0:len(array) - i]))))
    return print(array[-1])


if __name__ == '__main__':
    print(array)
    print(sorted(array))
    print(timeit.timeit(f'median_0({array})', setup='from __main__ import median_0', number=1000), 'Встроенная функция')
    print(timeit.timeit(f'median_1({array})', setup='from __main__ import median_1', number=1000), 'Сортировка')


