"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""
#isosceles triangle равнобедренным
#versatile triangle разносторонним
#equilateral triangle равносторонним
try:
    SIDE_A = int(input("Enter side A length: \n"))
    SIDE_B = int(input("Enter side B length: \n"))
    SIDE_C = int(input("Enter side C length: \n"))

except ValueError:
    print("Data is not correct")
    exit(1)


if SIDE_A + SIDE_B <= SIDE_C or SIDE_B + SIDE_C <= SIDE_A or SIDE_C + SIDE_A <= SIDE_B:
    print("This triangle does not exists")
elif SIDE_A != SIDE_B and SIDE_B != SIDE_C and SIDE_C != SIDE_A:
    print("This is versatile triangle")
elif SIDE_A == SIDE_B and SIDE_B == SIDE_C and SIDE_C == SIDE_A:
    print("This is equilateral triangle")
else:
    print("This is isosceles triangle")