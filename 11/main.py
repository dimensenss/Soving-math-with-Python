import pandas as pd
from math import exp
x0 = 0
y0 = 3

delta_x = 0.01

n = 10

def F(x):
    y = exp(-x)*(3*exp(x)*x**2+2*exp(x)*x+exp(x)+2)
    return y

data_X = [x0]
data_Y = [y0]
data_F = [F(x0)]

for i in range(n):
    data_X.append(x0 + delta_x)
    data_Y.append(delta_x*(3*x0**2+8*x0+3-y0)+y0)
    data_F.append(F(x0 + delta_x))

    y0 = delta_x*(3*x0**2+8*x0+3-y0)+y0
    x0 = x0 + delta_x

data = pd.DataFrame({'x': data_X, 'y(x)': data_Y, 'F(x)': data_F})
data.insert(loc=len(data.columns), column='F(x)-y(x)', value=data['F(x)']-data['y(x)'])

print(data)

data.to_excel('Cauchy_problem.xlsx')