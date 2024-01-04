from math import cos, sin, sqrt
import pandas as pd

# Визначаємо функцію
def F(x):
    y = cos(x)**3*sin(2.1*x)*(x**2+x+1)
    return y

x1 = -1
x4 = 0

# Поділяємо відрізок на 3 частини
phi = (sqrt(5) - 1) / 2
x2 = x4 - phi * (x4 - x1)
x3 = x1 + phi * (x4 - x1)

# Визначаємо точність розв'язку
h = 0.001

# Зберігаємо результати обчислень
data_X1 = [x1]
data_X2 = [x2]
data_X3 = [x3]
data_X4 = [x4]
data_F_X1 = [F(x1)]
data_F_X2 = [F(x2)]
data_F_X3 = [F(x3)]

data_F_X4 = [F(x4)]

# Перевіряємо досягнення точності
while x4 - x1 > h:
    min_value =min(F(x1), F(x2), F(x3), F(x4))
    # Звужуємо відрізок
    if F(x1) == min_value or F(x2) == min_value:
        x4 = x3
        x3 = x2
        x2 = x4 - phi * (x4 - x1)
    else:
        x1 = x2
        x2 = x3
        x3 = x1 + phi * (x4 - x1)

    # Зберігаємо результати обчислень
    data_X1.append(x1)
    data_X2.append(x2)
    data_X3.append(x3)
    data_X4.append(x4)
    data_F_X1.append(F(x1))
    data_F_X2.append(F(x2))
    data_F_X3.append(F(x3))
    data_F_X4.append(F(x4))

# Відображаємо результати обчислень
print('Результати обчислень')
print()

# Створюємо таблицю з результатами
data = pd.DataFrame({
    'x1': data_X1,
    'x2': data_X2,
    'x3': data_X3,
    'x4': data_X4,
    'F(x1)': data_F_X1,
    'F(x2)': data_F_X2,
    'F(x3)': data_F_X3,
    'F(x4)': data_F_X4
})

# Відображаємо всі стовпці
pd.set_option('display.max_columns', None)
print(data)

# Відображаємо наближений корінь рівняння
print()
print("Мінімум в точці с =", (x4 + x1) / 2, ", f(c) = ", F((x4 + x1) / 2))
data.to_excel('minimization_golden_ratio.xlsx')