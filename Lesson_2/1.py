"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


while True:

    SIGN = input('Enter operation sign. "0" for exit\n')

    if SIGN == '0':
        exit(0)
    elif SIGN not in '+-*/':
        continue
    try:
        NUM_A = int(input('Enter number A\n'))
        NUM_B = int(input('Enter number B\n'))
    except ValueError:
        print("Data is not correct")
        continue

    if SIGN == '+':
        print(f'{NUM_A} + {NUM_B} = {NUM_A + NUM_B}')
    elif SIGN == '-':
        print(f'{NUM_A} - {NUM_B} = {NUM_A - NUM_B}')
    elif SIGN == '*':
        print(f'{NUM_A} * {NUM_B} = {NUM_A * NUM_B}')
    elif SIGN == '/':
        try:
            print(f'{NUM_A} / {NUM_B} = {NUM_A / NUM_B}')
        except ZeroDivisionError:
            print("Can not divide by zero.")
            continue

#-----------------------------------------------------------------------


def math_operations():
    SIGN = input('Enter operation sign. "0" for exit\n')

    if SIGN == '0':
        exit(0)
    elif SIGN not in '+-*/':
        math_operations()

    try:
        NUM_A = int(input('Enter number A\n'))
        NUM_B = int(input('Enter number B\n'))
    except ValueError:
        print("Data is not correct")
        math_operations()

    if SIGN == '+':
        print(f'{NUM_A} + {NUM_B} = {NUM_A + NUM_B}')
        math_operations()
    elif SIGN == '-':
        print(f'{NUM_A} - {NUM_B} = {NUM_A - NUM_B}')
        math_operations()
    elif SIGN == '*':
        print(f'{NUM_A} * {NUM_B} = {NUM_A * NUM_B}')
        math_operations()
    elif SIGN == '/':
        try:
            print(f'{NUM_A} / {NUM_B} = {NUM_A / NUM_B}')
            math_operations()
        except ZeroDivisionError:
            print("Can not divide by zero.")
            math_operations()


math_operations()