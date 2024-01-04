from math import cos, sin
from numpy import sign
import pandas as pd

a = -1
b = 0.5
h = 0.001

def F(x):
    y = cos(x)**3*sin(2.1*x)*(x**2+x+1)
    return y

c = (a+b)/2

data_A = [a]
data_B = [b]
data_C = [c]
data_F_A = [F(a)]
data_F_B = [F(b)]
data_F_C = [F(c)]

while abs(F(c)) > h:
    if sign(F(c)) == sign(F(a)):
        a = c
    else:
        b = c
    c = (a+b)/2
    data_A.append(a)
    data_B.append(b)
    data_C.append(c)
    data_F_A.append(F(a))
    data_F_B.append(F(b))
    data_F_C.append(F(c))

data = pd.DataFrame({'a': data_A, 'F(a)': data_F_A, 'c': data_C, 'F(c)': data_F_C, 'b': data_B, 'F(b)': data_F_B})
print(data)
print("В точці с",c,',f(c) = ', F(c))