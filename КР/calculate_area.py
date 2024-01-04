
import matplotlib as plt

import pandas as pd

data_1 = pd.read_excel('Rovenkivskiy_simpson.xlsx')
data_2 = pd.read_excel('Rovenkivskiy_trapezoid.xlsx')
data_3 = pd.read_excel('Rovenkivskiy_boole.xlsx')
data_4 = pd.read_excel('area_1.xlsx')
data_5 = pd.read_excel('area_2.xlsx')
print(data_1)
print(data_2)
print(data_3)
print(data_4)
print(data_5)

data_1.plot('X', 'Y')
data_2.plot('X', 'Y')
data_3.plot('X', 'Y')
data_4.plot('X', 'Y')
data_5.plot('X', 'Y')

def Simpson_rule(data):
    h = data['X'][1]-data['X'][0]
    S = data['Y'][0]+data['Y'][len(data['X'])-1]
    for i in range(1,int((len(data['X'])-1)/2)+1):
        S= S+4*data['Y'][2*i-1]
    for i in range(1,int((len(data['X'])-1)/2)):
        S= S+2*data['Y'][2*i]
    return h*S/3

def trap_rule(data):
    h = data['X'][1]-data['X'][0]
    T = (data['Y'][0]+data['Y'][len(data['X'])-1])/2
    for i in range(1,len(data['X'])-1):
        T = T + data['Y'][i]
    return h*T

def Boole_rule(data):
    B = 0
    h = data['X'][1]-data['X'][0]
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
print("Simpson rule:",Simpson_rule(data_1))
print()
print("Trapezodial rule:",Simpson_rule(data_2))
print()
print("Boole rule:",Boole_rule(data_3))
print()
print("Trapezodial rule:",Simpson_rule(data_4))
print()
print("Trapezodial rule:",Simpson_rule(data_5))
print()