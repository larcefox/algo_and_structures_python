# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
print('--------------------eratosfen--------------------')

import timeit

# Наивный алгоритм
# T(n) = n^2


def erotosfen(i):
    simpl_num = list(range(2, i ** 2 + 1))
    for j in range(2, i ** 2 + 1):
        for k in simpl_num:
            if j != k and k % j == 0:
                del simpl_num[simpl_num.index(k)]
    return simpl_num


# Алгоритм с предустановленными константами
# T(n) = n


def erotosfen_lst(i):
    eratosfen_lst = list(range(2, i ** 2 + 1))
    sec = [2, 3, 5, 7, ]
    sec.extend([x for x in eratosfen_lst if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 9 != 0])
    return sec[i + 1]


# Алгоритм с предустановленными константами - лучший результат
# T(n) = n


def erotosfen_log(i):
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

# Решето
# T(n) = 4 + n * log(2n)

sec = 100

if __name__ == '__main__':
    print(timeit.timeit(f'erotosfen({sec})', setup='from __main__ import erotosfen', number=100))
    print(timeit.timeit(f'erotosfen_lst({sec})', setup='from __main__ import erotosfen_lst', number=100))
    print(timeit.timeit(f'erotosfen_log({sec})', setup='from __main__ import erotosfen_log', number=100))

# Изначаль попробовал использовать "del список[индекс]" но результаты оказались очень плохими
# во всех тестах наивный алгоритм на последнем месте, решето на втором, алгоритм с предустановленными константами на первом.