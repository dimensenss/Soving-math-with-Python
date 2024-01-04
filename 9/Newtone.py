from math import cos, sin
import pandas as pd

c = -1.204
h = 0.001

def F(x):
    y = cos(x)**3*sin(2.1*x)*(x**2+x+1)
    return y

def dF(x):
    return cos(x)**2*((-3)*(x**2+x+1)*sin(x)*sin(2.1*x)+2.1*(x**2+x+1)*cos(x)*cos(2.1*x)+(2*x+1)*sin(2.1*x)*cos(x))

data_C = [c]
data_F_C = [F(c)]

while abs(F(c)) > h:
    c = c - F(c)/dF(c)
    data_C.append(c)
    data_F_C.append(F(c))

data = pd.DataFrame({'c': data_C, 'F(c)': data_F_C})
print(data)
print("B точці c",c,',f(c) = ', F(c))