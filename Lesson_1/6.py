# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

FIRST_POSITION = ord("a") - 1

try:

    LIM1 = int(input("Enter letter number: \n"))

except ValueError:
    print("Data is not correct")
    exit(1)

print(f"You enter number of '{chr(LIM1 + FIRST_POSITION)}' letter")