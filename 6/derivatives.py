# Завантажуємо необхідні бібліотеки
import pandas as pd
import numpy as np
import math

# Визначаємо кінці відрізка та крок
a = -4
b = 4
h = 0.01

# Розбиваємо відрізок відповідно до кроку
ab = np.arange(a, b+h, h)

# Визначаємо задану функцію
def F(x):
    y = math.cos(x)**3 * math.sin(2.1*x) * (x**2+x+1)
    return y

# Здійснюємо табулювання функції
Y = []
for i in range(len(ab)):
    Y.append(F(ab[i]))

# Формуємо таблицю точок і значень функцій
data = pd.DataFrame({'X': ab, 'Y': Y})

# Чисельними методами визначаємо значення першої похідної
dY = []
dY.append((data['Y'][1]-data['Y'][0])/h)
for i in range(1, len(ab)-1):
    dY.append((data['Y'][i+1]-data['Y'][i-1])/(2*h))
dY.append((data['Y'][len(ab)-1]-data['Y'][len(ab)-2])/h)

# Додаємо до таблиці наближені значення першої похідної
data.insert(loc=len(data.columns), column='dY', value=dY)

# Аналітичний вираз першої похідної
def derF(x):
    y = math.cos(x)**2*((-3)*(x**2+x+1)*math.sin(x)*math.sin(2.1*x)+2.1*(x**2+x+1)*math.cos(x)*math.cos(2.1*x)+(2*x+1)*math.sin(2.1*x)*math.cos(x))
    return y

# Визначаємо точні значення першої похідної
dF = []
for i in range(len(ab)):
    dF.append(derF(ab[i]))

# Додаємо до таблиці точні значення першої похідної
data.insert(loc=len(data.columns), column='dF', value=dF)

# Визначаємо різницю між точними та наближеними значеннями першої похідної
delta_dF_dY = []
for i in range(len(ab)):
    delta_dF_dY.append(data["dF"][i]-data['dY'][i])

# Додаємо до таблиці різницю між точними та наближеними значеннями першої похідної
data.insert(loc=len(data.columns), column='dF-dY', value=delta_dF_dY)

# Чисельними методами визначаємо значення другої похідної
ddY = []
ddY.append((data['Y'][2]-2*data['Y'][1]+data['Y'][0])/h**2)
for i in range(1, len(ab)-1):
    ddY.append((data['Y'][i+1]-2*data['Y'][i]+data['Y'][i-1])/h**2)
ddY.append((data['Y'][len(ab)-3]-2*data['Y'][len(ab)-2]+data['Y'][len(ab)-1])/h**2)

# Додаємо до таблиці наближені значення другої похідної
data.insert(loc=len(data.columns), column='ddY', value=ddY)

# Аналітичний вираз другої похідної
def der_2_F(x):
    y = -4.41*(x**2+x+1)*math.sin(2.1*x)*math.cos(x)**3 + math.sin(2.1*x)*((x**2+x+1)*(6*math.sin(x)**2*math.cos(x)-3*math.cos(x)**3)+2*math.cos(x)**3-6*(2*x+1)*math.sin(x)*math.cos(x)**2) + 4.2*math.cos(2.1*x)*((2*x+1)*math.cos(x)**3-3*(x**2+x+1)*math.sin(x)*math.cos(x)**2)
    return y

# Визначаємо точні значення другої похідної
ddF = []
for i in range(len(ab)):
    ddF.append(der_2_F(ab[i]))

# Додаємо до таблиці точні значення другої похідної
data.insert(loc=len(data.columns), column='ddF', value=ddF)

# Визначаємо різницю між точними та наближеними значеннями другої похідної
delta_ddF_ddY = []
for i in range(len(ab)):
    delta_ddF_ddY.append(data["ddF"][i]-data['ddY'][i])

# Додаємо до таблиці різницю між точними та наближеними значеннями другої похідної
data.insert(loc=len(data.columns), column='ddF-ddY', value=delta_ddF_ddY)

# Відображаємо всі стовпці таблиці
print(data)

# Зберігаємо данні у файл Excel
data.to_excel('derivatives.xlsx')