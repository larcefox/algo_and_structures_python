# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.


try:

    YEAR = int(input("Enter year: \n"))

except ValueError:
    print("Data is not correct")
    exit(1)

Y_IS_B = 'Year is bissextile' if (YEAR % 4 == 0 and YEAR % 100 != 0) or YEAR % 400 == 0 \
    else 'Year is not bissextile'
print(Y_IS_B)