"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from datetime import datetime


def num_choise_cycle():
    num = int(int(datetime.now().strftime("%f"))/10000)
    moves = 10
    for i in range(moves):
        try:
            gues = int(input('Enter number:\n'))
        except ValueError:
            print("Data is incorrect!")
            continue
        if gues == num:
            return print(f"You made it! The number is: {num}")
        elif gues < num:
            print(f"The hidden number is greater! Number of try: {i + 1}.")
        elif gues > num:
            print(f"The hidden number is lower! Number of try: {i + 1}.")
    else:
        return print("You lose!")


num_choise_cycle()

#-----------------------------------------------------------------------------------


def num_choise_rec():
    num = int(int(datetime.now().strftime("%f"))/10000)
    moves = 10
    rec(num, moves)


def rec(num, moves):
    if moves == 0:

        return print("You lose!")

    moves -= 1

    try:
        gues = int(input('Enter number:\n'))
    except ValueError:
        print("Data is incorrect!")
        return rec(num, moves)

    if gues == num:
        return print(f"You made it! The number is: {num}")
    elif gues < num:
        print(f"The hidden number is greater! Number of try: {10 - moves}.")
        rec(num, moves)
    elif gues > num:
        print(f"The hidden number is lower! Number of try: {10 - moves}.")
        rec(num, moves)


num_choise_rec()

