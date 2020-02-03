"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
from collections import Counter
import hashlib


string = list('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') # пocтoяннoe cчacтьe (нем.)
hash_obj = hashlib.md5()

#example
'''
length = len(string)

for start in range(length):

    if start == 0:
        length = len(string) - 1
    else:
        length = len(string)

    for end in range(length, start, -1):
        print(string[start:end])
'''

s = 0
substring = Counter()

for letter_start in range(len(string)):

    if s == 0:
        e = len(string) - 1
    else:
        e = len(string)

    for letter_end in range(e - s):

        hash_obj.update(''.join(string[s:e]).encode())
        substring[hash_obj.hexdigest()] += 1
        if len(string[s:e]) == 1:
            print(string[s:e], hash_obj.hexdigest())
        e -= 1
    s += 1

print(substring, len(substring))
