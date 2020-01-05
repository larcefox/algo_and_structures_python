#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

FIRST_POSITION = ord("a") - 1

LIM1 = ord(input("Enter first letter: \n"))
LIM2 = ord(input("Enter last letter: \n"))

print(f"First letter has position: {LIM1 - FIRST_POSITION}")
print(f"Last letter has position: {LIM2 - FIRST_POSITION}")
print(f"Difference betwin letters: "
      f"{abs(LIM2 - LIM1) if LIM1 != LIM2 else 'letters are the same'}")