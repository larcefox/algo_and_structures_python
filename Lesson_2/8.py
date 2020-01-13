"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

NUM_STR = ''
NUM_QUANT = 0

try:
    QUANT = int(input('Enter quantity of numbers:\n'))
except ValueError:
    print("Data is incorrect!")

for i in range(QUANT):
    try:
        NUM_STR += str(int(input(f'Enter  number {i + 1}:\n')))
    except ValueError:
        print("Data is incorrect!")
        continue

try:
    NUM = int(input('Enter seeking number:\n'))
except ValueError:
    print("Data is incorrect!")

#-----------------------------------------------------------------


for i in NUM_STR:
    if NUM == int(i):
        NUM_QUANT += 1

print(f'{NUM}: {NUM_QUANT}')

#------------------------------------------------------------------

NUM_QUANT = 0
NUM_STR = int(NUM_STR)


def seek(num, num_str, num_quant):
    if num_str == 0:
        return print(f'{num}: {num_quant}')

    if num_str % 10 == num:
        num_quant += 1

    num_str = num_str // 10
    seek(num, num_str, num_quant)


seek(NUM, NUM_STR, NUM_QUANT)
