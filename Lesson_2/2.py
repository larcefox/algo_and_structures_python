"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

try:
    NUM_A = int(input('Enter number\n'))
except ValueError:
    print("Data is not correct")
    exit(1)

#-----------------------------------------------------------------------

EVEN = 0
ODD = 0
TEMP = 0


while NUM_A > 0:

    TEMP = NUM_A % 10
    if TEMP % 2 == 0:
        EVEN += 1
    else:
        ODD += 1
    NUM_A = NUM_A // 10

print(f'Even numbers:{EVEN}, odd numbers:{ODD}.')

#-----------------------------------------------------------------------


def even_counter(num, even, odd):

    if num == 0:
        return print(f'Even numbers:{even}, odd numbers:{odd}.')

    temp = num % 10

    if temp % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

    even_counter(num, even, odd)


even_counter(NUM_A, EVEN, ODD)
