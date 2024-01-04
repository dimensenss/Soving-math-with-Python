
import pandas as pd
from gaussMethod import Gauss

# Завантажуємо дані
data = pd.read_excel('Tricubic_Interpolation.xlsx')

# Визначаємо степені кожної змінної                  
power_X = len(data.X.unique()) - 1
power_Y = len(data.Y.unique()) - 1
power_Z = len(data.Z.unique()) - 1

# Формуємо матрицю A
A = []
for j in range((power_X+1) * (power_Y+1) * (power_Z+1)):
    s = []
    for i in range(power_X, -1, -1):
        for k in range(power_Y, -1, -1):
            for l in range(power_Z, -1, -1):
                s.append((data['X'][j]**i)*(data['Y'][j]**k)*(data['Z'][j]**l))
    A.append(s)

# Формуємо вектор b
b = []
for j in range((power_X+1) * (power_Y+1) * (power_Z+1)):
    b.append(data['F'][j])

# Обчислюємо коефіцієнти полінома
c = Gauss(A,b)

# Формуємо поліном
polynom_string = 'P(x,y,z) = '
j = 0
for i in range(power_X, -1, -1):
    for k in range(power_Y, -1, -1):
        for l in range(power_Z, -1, -1):
            polynom_string = polynom_string + str(c[j]) + '*x^' + str(i) + '*y^' + str(k) + '*z^' + str(l) + '+'
            j = j + 1
polynom_string = polynom_string[:-9].replace('+-', '-').replace('x^1', 'x').replace('y^1', 'y').replace('z^1', 'z')
polynom_string = polynom_string.replace('*x^0', '').replace('*y^0', '').replace('*z^0', '')

# Відображаємо поліном
print('Інтерполяційний поліном')
print(polynom_string)