# завантажуємо необхідну бібліотеку 
import pandas as pd
# Завантажуємо необхідну функцію
from gaussMethod import Gauss 
# Матриця А та вектор b
A = [[ 4,-1, 0,-1, 0, 0, 0, 0, 0], 
     [-1, 4,-1, 0,-1, 0, 0, 0, 0], 
     [ 0,-1, 4, 0, 0,-1, 0, 0, 0], 
     [-1, 0, 0, 4,-1, 0,-1, 0, 0],
     [ 0,-1, 0,-1, 4,-1, 0,-1, 0],
     [ 0, 0,-1, 0,-1, 4, 0, 0,-1], 
     [ 0, 0, 0,-1, 0, 0, 4,-1, 0], 
     [ 0, 0, 0, 0,-1, 0,-1, 4,-1],
     [ 0, 0, 0, 0, 0,-1, 0,-1, 4]]

b = [-3.625, 2.5, 54.875, -2.5, -7.25, 36.5, 24.875, 21.5, 83.375]
# Знаходимо розв'язок системи рівнянь 
c = Gauss (A,b)
# Визначаємо границі по Х
x_0 = 0
x_n = 1
# Визначаемо границі по у 
y_0 = 0
y_n = 1
# Визначаємо кількість точок по X та У
n_x=3
n_y=3
# Визначаємо крок по X та Y 
delta_x = (x_n - x_0)/(n_x+1) 
delta_y = (y_n - y_0)/(n_y+1) 
#Визначаемо точки У
data_Y = [y_0]
for i in range (1,n_y+1):
     data_Y.append(y_0 + 1*delta_y)
data_Y.append(y_n)

#Значення функції для х_0
data_x_0 = [0,2.4375,9.75,21.9375,39]
#Значення функції для х_1
data_x_1 = [1.1875]
data_x_1 = data_x_1 + c[:3] 
data_x_1.append(40.1875) 
#значення функції для x_2
data_x_2 = [4.75]
data_x_2 = data_x_2 + c[3:6] 
data_x_2.append(43.75)
#Значення функції для x_3 
data_x_3 = [10.6875]
data_x_3 = data_x_3 + c[6:] 
data_x_3.append(49.6875)
# Значення функції для x_4
data_x_4 = [19,21.4375,28.75,40.9375,58] 
#формуемо результати наближених обчислень
data = pd.DataFrame({'y': data_Y, 'x=0': data_x_0,
                    '0.25': data_x_1, '0.5': data_x_2,
                    '0.75': data_x_3, '1.0': data_x_4})
# відображаемо результати наближених обчислень 
print('Результати наближених обчислень')
print(data)
# зберігаємо результати наближених обчислень 
data.to_excel('elliptic_number.xlsx')
# функція, що визначає точний розв'язок 
def F_exact (x,y):
     z = 19*x**2 +39*y**2
     return z
# обчислюемо точні значення 
data_F_X_Y = []
for j in range (n_x+2) :
     s = []
     for i in range (n_y+2):
          s.append (F_exact (x_0 + j*delta_x, y_0 + i*delta_y))
     data_F_X_Y.append(s)
          
#формуємо результати точних обчислень
data_exact = pd.DataFrame({'y': data_Y,
                           'x=' + str(x_0): data_F_X_Y[0]})
for j in range (1, n_y+2):
     data_exact.insert (loc=len(data_exact.columns),
                        column=str(y_0+j*delta_y), 
                        value=data_F_X_Y[j])
# відображаемо результати точних обчислень 
print('Результати точних обчислень')
print(data_exact)
# Зберігаємо результати точних обчислень
data_exact.to_excel('elliptic_exact.xlsx')
# обчислюемо різницю між точними та наближеними обчисленнями 
data_errors = data_exact - data
# відображаемо різницю між точними та наближеними обчисленнями
print('Різниця між точними та наближеними обчисленнями') 
print(data_errors)
# Зберігаємо різницю між точними та наближеними обчисленнями 
data_errors.to_excel('elliptic_errors.xlsx')