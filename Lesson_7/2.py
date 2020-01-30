"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random
import timeit

array = [random.randint(0, 50) for _ in range(50000)]
array1 = list(array)
array2 = list(array)


def merge_sort(array):
    if len(array) > 1:
        center = len(array) // 2
        left = array[:center]
        right = array[center:]

        merge_sort(left)
        merge_sort(right)

        l, r, a = 0, 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[a] = left[l]
                l += 1
            else:
                array[a] = right[r]
                r += 1
            a += 1

        while l < len(left):
            array[a] = left[l]
            l += 1
            a += 1

        while r < len(right):
            array[a] = right[r]
            r += 1
            a += 1

        return array


def merge_sort1(array):
    if len(array) > 1:
        center = len(array) // 2
        left = array[:center]
        right = array[center:]

        i = 1
        k = 1

        while i < len(left):
            for j in range(len(left) - i):
                if left[j] > left[j + 1]:
                    left[j], left[j + 1] = left[j + 1], left[j]
            i += 1

        while k < len(right):
            for j in range(len(right) - k):
                if right[j] > right[j + 1]:
                    right[j], right[j + 1] = right[j + 1], right[j]
            k += 1

        l, r, a = 0, 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[a] = left[l]
                l += 1
            else:
                array[a] = right[r]
                r += 1
            a += 1

        while l < len(left):
            array[a] = left[l]
            l += 1
            a += 1

        while r < len(right):
            array[a] = right[r]
            r += 1
            a += 1

        return array


def merge_sort2(array):
    if len(array) > 1:
        center = len(array) // 2
        left = array[:center]
        right = array[center:]

        merge_sort2(left)
        merge_sort2(right)

        i = 1

        while i < len(array):
            for j in range(len(array) - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            i += 1


        return array

if __name__ == '__main__':
    print(array)
    print(timeit.timeit(f'print(merge_sort({array}))', setup='from __main__ import merge_sort', number=1), 'Обычный')
    print(array1)
    print(timeit.timeit(f'print(merge_sort1({array1}))', setup='from __main__ import merge_sort1', number=1), 'Гибридный')
    print(array2)
    print(timeit.timeit(f'print(merge_sort2({array2}))', setup='from __main__ import merge_sort2', number=1), 'Гибридный 2')
