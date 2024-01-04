# Завантажуємо необхідну бібліотеку
import pandas as pd
# Визначаємо границі по X
x_0 = 0
x_n = 1
# Визначаємо границі по Y
y_0 = 0
y_n = 1
# Визначаємо кількість точок по X та Y
n_x = 9
n_y = 9
# Визначаємо крок по X та Y
delta_x = (x_n - x_0)/(n_x+1)
delta_y = (y_n - y_0)/(n_y+1)
# Визначаємо точки X
data_X = [x_0]
for i in range(1,n_x+1):
    data_X.append(x_0 + i*delta_x)
data_X.append(x_n)
# Функція, що визначає початкові умови
def F(x):
    y = 19*x**2 
    return y
# Обчислюємо початкові умови
data_Y_0 = []
for i in range(0,n_x+2):
    data_Y_0.append(F(data_X[i]))
# Зберігаємо точки X та початкові умови
data = pd.DataFrame({'x': data_X, 'y=' + str(y_0): data_Y_0})
# Обчислюємо значення у наступних точках Y та зберігаємо результати
for j in range(1, n_y+2):
    # Лівий кінець відрізка 
    data_Y_i = [data.iloc[0,j]+(39*delta_y)*(data.iloc[2,j]-2*data.iloc[1,j]+data.iloc[0,j])/(38*delta_x**2)]
    # Внутрішні точки відрізка
    for i in range(1,n_x+1):
        data_Y_i.append(data.iloc[i,j]+(39*delta_y)*(data.iloc[i+1,j]-2*data.iloc[i,j]+data.iloc[i-1,j])/(38*delta_x**2))
    # Правий кінець відрізка
    data_Y_i.append(data.iloc[n_x+1,j]+(39*delta_y)*(data.iloc[n_x+1,j]-2*data.iloc[n_x,j]+data.iloc[n_x-1,j])/(38*delta_x**2))
    # Зберігаємо результати обчислень
    data.insert(loc=len(data.columns), column=str(y_0+j*delta_y), value=data_Y_i)
# Відображаємо результати наближених обчислень
print('Результати наближених обчислень')
print(data)
# Зберігаємо результати наближених обчислень
data.to_excel('parabolic_number.xlsx')
# Функція, що визначає точний розв'язок
def F_exact(x,y):
    z = 19*x**2 + 39*y
    return z
# Обчислюємо точні значення
data_F_X_Y = []
for j in range(n_y+2):
    s = []
    for i in range(n_x+2):
        s.append(F_exact(x_0 + i*delta_x, y_0 + j*delta_y))
    data_F_X_Y.append(s)
# Формуємо результати точних обчислень
data_exact = pd.DataFrame({'x': data_X, 'y=' + str(y_0): data_F_X_Y[0]})
for j in range(1, n_y+2):
    data_exact.insert(loc=len(data_exact.columns), column=str(y_0+j*delta_y), value=data_F_X_Y[j])
# Відображаємо результати точних обчислень
print('Результати точних обчислень')
print(data_exact)
# Зберігаємо результати точних обчислень
data_exact.to_excel('parabolic_exact.xlsx')
# Обчислюємо різницю між точними та наближеними обчисленнями
data_errors = data_exact - data
# Відображаємо різницю між точними та наближеними обчисленнями
print('Різниця між точними та наближеними обчисленнями')
print(data_errors)
# Зберігаємо різницю між точними та наближеними обчисленнями
data_errors.to_excel('parabolic_errors.xlsx')

