м# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import timeit


def multiple_check():
    return [sum(1 if x % y == 0 else 0 for x in range(2, 100)) for y in range(2, 10)]

# T(n) = n^2 (два цикла) + 1 (вычисление суммы списка)
# ~ 0.0002 milliseconds
#------------------------------------------------------------------------------------

def multiple_check_rec(sec):

  if len(sec) == 0:
    return
  _ = 99 // sec.pop(0)
  multiple_check_rec(sec)

# T(n) = 2n
# Возврат константы и вычисление константы "_"
# ~ 1.2995 milliseconds без мемоизации
#------------------------------------------------------------------------------------


if __name__ == '__main__':
  print(timeit.timeit('multiple_check()', setup='from __main__ import multiple_check', number=100))
  print(timeit.timeit('multiple_check_rec(list(range(2, 10)))', setup= 'from __main__ import multiple_check_rec', number=100))

#Выводы:
# При небольшом колличестве повторений лучше использовать вложенные генераторы,
# но даже при 10 повторениях рекурсия показывает лучше время, чем генераторы.