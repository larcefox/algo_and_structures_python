# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).
try:
    
    NUM_A = int(input("Enter number A: \n"))
    NUM_B = int(input("Enter number B: \n"))
    NUM_C = int(input("Enter number C: \n"))

except ValueError:
    print("Data is not correct")
    exit(1)

if NUM_A > NUM_B > NUM_C or NUM_C > NUM_B > NUM_A:
    print('B number is middle')
elif NUM_B > NUM_C > NUM_A or NUM_A > NUM_C > NUM_B:
    print('C number is middle')
else:
    print('A number is middle')
