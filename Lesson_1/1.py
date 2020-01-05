# 1.      Найти сумму и произведение цифр трехзначного числа, которое
# вводит пользователь.

NUM = int(input('Enter number \n'))

NUM_A = NUM // 100
NUM_B = (NUM // 10) % 10
NUM_C = NUM % 10
print(f"Произведение чисел: {NUM_A}, {NUM_B}, {NUM_C} равно {NUM_A * NUM_B * NUM_C}")
print(f"Сумма чисел: {NUM_A}, {NUM_B}, {NUM_C} равно {NUM_A + NUM_B + NUM_C}")
