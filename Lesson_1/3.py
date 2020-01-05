# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

X1 = int(input('x1 \n'))
X2 = int(input('x2 \n'))
Y1 = int(input('y1 \n'))
Y2 = int(input('y2 \n'))

K_PARAM = (Y2 - Y1) / (X2 - X1)
B_PARAM = Y2 - K_PARAM * X2
print(f"y = {K_PARAM}x +{B_PARAM}")