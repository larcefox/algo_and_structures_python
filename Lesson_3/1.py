# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def multiple_check():
    return print([sum(1 if x % y == 0 else 0 for x in range(2, 100)) for y in range(2, 10)])


multiple_check()
