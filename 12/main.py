
# Завантажуємо необхідну функцію
from gaussMethod import Gauss
# Завантажуємо бібліотеку
import pandas as pd
from math import exp,e
# Визначаємо крайові умови
a = 0
Y_a = 4
b = 1
Y_b = 5+3*exp(1)
# Визначаємо кількість точок
n = 7
# Визначаємо крок
delta_x = (b-a)/(n+1)
# Визначаємо точний розв'язок
def F(x):
    y = 3*x**2+x+3*exp(x)+1
    return y
# Зберігаємо точки
data_X = [a]
for i in range(1,n+1):
    data_X.append(a+i*delta_x)
data_X.append(b)
# Зберігаємо точні значення
data_F = []
for i in range(n+2):
    data_F.append(F(data_X[i]))
# Створюємо нульову матрицю А та нульовий вектор B
s = [0]*n
A = []
for i in range(n):
    A.append(s[:])
B = s[:]

A[0][0] = -4
A[0][1] = 2 - delta_x
B[0] = 2 * (delta_x**2) * (-6 * (a+delta_x) + 5) - (2 + delta_x) * Y_a

# Коефіцієнти наступних рівнянь
for i in range(1, n - 1):
    A[i][i - 1] = 2 + delta_x
    A[i][i] = -4
    A[i][i + 1] = 2 - delta_x
    B[i] = 2 * (delta_x**2) * (-6 * (a + (i + 1) * delta_x) + 5)

# Коефіцієнти останнього рівняння
A[n - 1][n - 2] = 2 + delta_x
A[n - 1][n - 1] = -4
B[n - 1] = 2 * (delta_x**2) * (-6 * (a + n * delta_x) + 5) - (2 - delta_x) * Y_b



# Знаходимо розв'язок системи рівнянь
C = Gauss(A,B)
# Зберігаємо наближені значення
data_Y = [Y_a]
data_Y = data_Y + C
data_Y.append(Y_b)
# Відображаємо результати обчислень
print('Результати обчислень')
data = pd.DataFrame({'x': data_X, 'y(x)': data_Y, 'F(x)': data_F})
data.insert(loc=len(data.columns),
            column='F(x)-y(x)', value=data['F(x)']-data['y(x)'])
print(data)
# Зберігаємо результати обчислень
data.to_excel('boundary_value_problem.xlsx')