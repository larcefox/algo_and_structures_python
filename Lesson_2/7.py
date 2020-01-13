"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

try:
    NUM_N = int(input('Enter number:\n'))
except ValueError:
    print("Data is incorrect!")

#-----------------------------------------------------------------------

SUMM = 0
TEMP_N = 0

def sec(n, temp_n, summ):

    if temp_n == n:
        return print(summ == n * (n + 1)/2)
    temp_n += 1
    summ = summ + temp_n
    sec(n, temp_n, summ)

sec(NUM_N, TEMP_N, SUMM)

#-----------------------------------------------------------------------

SUMM = 0

for i in range(1, NUM_N + 1):
    SUMM += i
else:
    print(SUMM == NUM_N * (NUM_N + 1) / 2)