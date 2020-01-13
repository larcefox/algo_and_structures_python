"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
try:
    NUM = int(input('Enter number\n'))
except ValueError:
    print("Data is not correct")
    exit(1)
SEQ = 1
SUMM = 0
CFFT = -2

while NUM > 0:
    SUMM += SEQ
    SEQ = SEQ / CFFT
    NUM -= 1

print(SUMM)

#-----------------------------------------------------------------------


def seq_summ(num, cfft, seq, summ):

    if num <= 0:
        return print(summ)

    summ += seq
    seq = seq / cfft
    num -= 1

    seq_summ(num, cfft, seq, summ)


seq_summ(NUM, CFFT, SEQ, SUMM)
