'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
 Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
'''

'''
Проанализировал почти все написанные алгоритмы. 
При использовании memory_profiler инкременты памяти возникают только при
создании новых переменных внутри функции. Как в "решете Эратосфена".
По guppy нашел массу примеров. Сделал самый простой. Total size = 22043 bytes
'''

import random
from guppy import hpy
from memory_profiler import profile

hp = hpy()
#hp.setref()


start_size = hp.heap()

@profile
def erotosfen_log():
    i = 100
    l = i ** 2 + 1
    eratosfen_lst = list(range(l))
    eratosfen_lst[1] = 0
    n = 2

    while n < l:
        if n > 0:
            j = n * 2
            while j < l:
                eratosfen_lst[j] = 0
                j +=n
        n += 1
    return [x for x in eratosfen_lst if x > 0][i + 1]


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


@profile
def merge():
    array = [random.randint(0, 50) for _ in range(1000)]
    merge_sort2(array)


if __name__ == '__main__':
    erotosfen_log()
    merge()
    print(hp.heap() - start_size)


'''
Line #    Mem usage    Increment   Line Contents
================================================
    25     60.6 MiB     60.6 MiB   @profile
    26                             def erotosfen_log():
    27     60.6 MiB      0.0 MiB       i = 100
    28     60.6 MiB      0.0 MiB       l = i ** 2 + 1
    29     60.8 MiB      0.3 MiB       eratosfen_lst = list(range(l))
    30     60.8 MiB      0.0 MiB       eratosfen_lst[1] = 0
    31     60.8 MiB      0.0 MiB       n = 2
    32                             
    33     60.8 MiB      0.0 MiB       while n < l:
    34     60.8 MiB      0.0 MiB           if n > 0:
    35     60.8 MiB      0.0 MiB               j = n * 2
    36     60.8 MiB      0.0 MiB               while j < l:
    37     60.8 MiB      0.0 MiB                   eratosfen_lst[j] = 0
    38     60.8 MiB      0.0 MiB                   j +=n
    39     60.8 MiB      0.0 MiB           n += 1
    40     60.8 MiB      0.0 MiB       return [x for x in eratosfen_lst if x > 0][i + 1]


Filename: /home/larce/Documents/GeekBrains/Algorithms/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    64     60.8 MiB     60.8 MiB   @profile
    65                             def merge():
    66     60.8 MiB      0.0 MiB       array = [random.randint(0, 50) for _ in range(1000)]
    67     60.8 MiB      0.0 MiB       merge_sort2(array)


Partition of a set of 127 objects. Total size = 22043 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0     94  74     9495  43      9495  43 str
     1      2   2     7872  36     17367  79 _sre.SRE_Pattern
     2      1   1     1152   5     18519  84 list
     3      4   3      960   4     19479  88 dict of function
     4      5   4      680   3     20159  91 function
     5      7   6      512   2     20671  94 tuple
     6      2   2      480   2     21151  96 dict (no owner)
     7      1   1      432   2     21583  98 types.FrameType
     8      8   6      384   2     21967 100 builtins.cell
     9      2   2       48   0     22015 100 float
    10      1   1       28   0     22043 100 int
'''