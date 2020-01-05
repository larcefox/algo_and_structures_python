"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
from random import random

LIM1 = int(input("Enter low limit: \n"))
LIM2 = int(input("Enter hi limit: \n"))
RNUM = int(random() * (LIM2 - LIM1 + 1) + LIM1)
print(RNUM)

LIM1 = int(input("Enter low limit: \n"))
LIM2 = int(input("Enter hi limit: \n"))
RNUM = random() * (LIM2 - LIM1 + 1) + LIM1
print(RNUM)

LIM1 = ord(input("Enter first letter: \n"))
LIM2 = ord(input("Enter last letter: \n"))
RLET = int(random() * (LIM2 - LIM1 + 1) + LIM1)
print(chr(RLET))