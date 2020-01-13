"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

try:
    NUM_A = int(input('Enter number\n'))
except ValueError:
    print("Data is not correct")
    exit(1)

NUM_B = ''

#-----------------------------------------------------------------------

while NUM_A != 0:
    NUM_B += str(NUM_A % 10)
    NUM_A = NUM_A // 10

print(f'Reverse number:{NUM_B}.')

#-----------------------------------------------------------------------


def reverse_a(num_a, num_b):
    if num_a == 0:
        return print(f'Reverse number:{num_b}.')
    num_b += str(num_a % 10)
    num_a = num_a // 10
    reverse_a(num_a, num_b)


reverse_a(NUM_A, NUM_B)