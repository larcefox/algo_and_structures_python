"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict

hex_num = d = defaultdict(list)
for i in range(2):
    hex_num[i].extend(list(input('Enter number:\n').upper()))

    for simbol in hex_num[i]:
        if simbol not in '0123456789ABCDEF':
            print("Data is incorrect!")
            exit(1)

summ = hex(sum(int(''.join(j), 16) for j in hex_num.values())).upper()
mull = hex(list(int(''.join(j), 16) for j in hex_num.values())[0] * list(int(''.join(j), 16) for j in hex_num.values())[1])

print(summ, mull)

#-----------------------------------------------------------------------------------------------------------------------------

class HexSumMul:
    def __init__(self, hex_num_c):
        self.hex_num_c = hex_num_c

    def __add__(self, other):
        return hex(int(''.join(self.hex_num_c), 16) + int(''.join(other.hex_num_c), 16)).upper()

    def __mul__(self, other):
        return hex(int(''.join(self.hex_num_c), 16) * int(''.join(other.hex_num_c), 16)).upper()


hex_num_st = HexSumMul(list(input('Enter number:\n').upper()))
hex_num_nd = HexSumMul(list(input('Enter number:\n').upper()))


hex_sum = hex_num_st + hex_num_nd
hex_mul = hex_num_st * hex_num_nd

print(hex_sum, hex_mul)