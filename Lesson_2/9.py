"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

TEMP = 0
NUM = 0
NUM_SUMM = 0
CURRENT_NUM = 0
BIGEST_NUM = 0

try:
    QUANT = int(input('Enter quantity of numbers:\n'))
except ValueError:
    print("Data is incorrect!")

for i in range(QUANT):
    try:
        NUM = int(input(f'Enter  number {i + 1}:\n'))
    except ValueError:
        print("Data is incorrect!")
        continue
    CURRENT_NUM = NUM
    while NUM != 0:
        TEMP += NUM % 10
        NUM = NUM //10
    if TEMP > NUM_SUMM:
        NUM_SUMM = TEMP
        BIGEST_NUM = CURRENT_NUM
        TEMP = 0
else:
    print(BIGEST_NUM, NUM_SUMM)

#----------------------------------------------------------------------------

