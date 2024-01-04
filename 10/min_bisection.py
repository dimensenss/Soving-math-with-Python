
from math import cos, sin
import pandas as pd

# Визначаємо функцію
def F(x):
    y = cos(x)**3*sin (2.1*x)*(x**2+x+1)
    return y
# Визначаємо границі відрізку
x1=-1
x5 =0
# Поділяємо відрізок на 4 частини
x3 = (x1+x5) /2
x2 = (x1+x3)/2
x4 = (x3+x5) /2

# Визначаємо точнічть розв'язку
h = 0.001
# Зберігаємо результати обчислень
data_X1 = [x1]
data_X2 = [x2]
data_X3 = [x3]
data_X4 = [x4]
data_X5 = [x5]
data_F_X1 = [F(x1)]
data_F_X2 = [F(x2)]
data_F_X3 = [F(x3)]
data_F_X4 = [F(x4)]
data_F_X5 = [F(x5)]
#Перевіряємо досягнення точності
while x5 - x1 > h:
    min_value = min(F(x1), F(x2), F(x3), F(x4), F(x5))
    
    # Звужуємо відрізок
    if F(x1) == min_value or F(x2) == min_value:
        x5 = x3
        x3 = x2
    elif F(x3) == min_value:
        x1 = x2
        x5 = x4
    else:
        xl = x3
        x3 = x4
    # Поділяємо відрізок на 4 частини
    x2 = (x1+x3)/2
    x4 = (x3+x5)/2
    # Зберігаємо результати обчислень
    data_X1.append(x1)
    data_X2.append(x2)
    data_X3.append(x3)
    data_X4.append(x4)
    data_X5.append(x5)
    data_F_X1.append(F(x1))
    data_F_X2.append(F(x2))
    data_F_X3.append(F(x3))
    data_F_X4.append(F(x4))
    data_F_X5.append(F(x5))
# Відображаємо результати обчислень
print("Результати обчислень")
print()
data = pd.DataFrame({'x1': data_X1,
                    'x2': data_X2,
                    'x3': data_X3,
                    'x4': data_X4,
                    'x5': data_X5,
                    'F(x1)': data_F_X1,
                    'F(x2)': data_F_X2,
                    'F(x3)': data_F_X3,
                    'F(x4)': data_F_X4,
                    'F(x5)': data_F_X5})
# Відображаємо всі стовпці
pd.set_option('display.max_columns', None)
print (data)
# Відображаємо наближений корінь рівняння
print ()
print ('Мінімум в точці с =',x3, 'f(c) = ', F(x3))
# Зберігаємо результати обчислень
data.to_excel ('minimization_bisection.xlsx')