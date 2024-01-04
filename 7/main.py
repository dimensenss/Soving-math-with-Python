import pandas as pd
import numpy as np
import math
a=-4
b=4
h=0.01
X = np.arange(a, b+h, h)

# Визначаємо задану функцію
def F(x):
    y = math.cos(x)**3 * math.sin(2.1*x) * (x**2+x+1)
    #y = math.cos(x)*math.sin(x)*(x**2+x+1)
    return y
Y = []
for i in range(len(X)):
    Y.append(F(X[i]))

# Формуємо таблицю точок і значень функцій
data = pd.DataFrame({'X': X, 'Y': Y})
print(data)
#Метод трапецій
def trap_rule(data,h):
    T = (data['Y'][0]+data['Y'][len(X)-1])/2
    for i in range(1,len(X)-1):
        T = T+data['Y'][i]
    return h*T
#Метод Сімпсона
def Simpson_rule(data,h):
    S= (data['Y'][0]+data['Y'][len(X)-1])
    for i in range(1,int((len(X)-1)/2)+1):
        S= S+4*data['Y'][2*i-1]
    for i in range(1,int((len(X)-1)/2)):
        S= S+2*data['Y'][2*i]
    return h*S/3
#Метод Буля
def Boole_rule(data,h):
    B = 0
    for i in range(0, len(data)):
        if i == 0 or i == len(data)-1:
            B += 7 * data['Y'][i]
        elif i % 2 != 0:
            B += 32 * data['Y'][i]
        elif i % 2 == 0 and i % 4 != 0:
            B += 12 * data['Y'][i]
        elif i % 4 == 0:
            B += 14 * data['Y'][i]
    return 2*h*B/ 45



print()
print(f'Trapezoidal_rule {trap_rule(data, h)}')
print(f'Simpson_rule {Simpson_rule(data, h)}')
print(f'Boole/s rule {Boole_rule(data, h)}')