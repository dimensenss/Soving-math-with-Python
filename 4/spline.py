from gaussMethod import Gauss
x = [0, 0.5, 1, 2, 3.5, 4, 6]
f = [-15.351, 1.396, 34.206, 82.917, 57.901, 98.128, 123.178]
d = len(x)

s = [0]*4*(d-1)
A = []
for i in range(4*(d-1)):
    A.append(s[:])
b = s[:]

for j in range(d-1):
    for i in range(4):
        A[j][i+4*j] = (x[j]-x[j+1])**i
    b[j] = f[j]

for j in range(d-1, 2*(d-1)):
    A[j][4*(j-(d-1))] = 1
    b[j] = f[1+(j-(d-1))]

for j in range(2*(d-1), 3*d-4):
    for i in range(4):
        if i == 0:
            A[j][1+4*(j-2*(d-1))] = -1
        else:
            A[j][i+4+4*(j-2*(d-1))] = i*(x[1+j-2*(d-1)]-x[2+j-2*(d-1)])**(i-1)

for j in range(3*d-4, 4*d-6):
    A[j][2+4*(j-(3*d-4))] = -2
    A[j][6+4*(j-(3*d-4))] = 2
    A[j][7+4*(j-(3*d-4))] = 6*(x[1+(j-(3*d-4))]-x[2+(j-(3*d-4))])

A[4*d-6][2] = 2
A[4*d-6][3] = 6*(x[0]-x[1])
A[4*d-5][-2] = 2

print('Матриця А')
for i in range(len(A)):
    print(A[i])
print('Вектор b')
print(b)

c = Gauss(A,b)

print()
print('Вектор коефіцієнтів')
print(c)

print()
print('Коефіцієнти сплайнів')
for i in range(d-1):
    print(c[4*i:4*i+4])

print()
print('Сплайни')
for j in range(d-1):
    spline = 'S_' + str(j+1) + '(x) = ' + str(c[0+4*j]) + '+'
    for i in range(1, 4):
        spline = spline + str(c[i+4*j]) + '*(x-' + str(x[j+1]) + ')^' + str(i) + '+'
    spline = spline[:-1].replace('+-', '-').replace('^1', '')
    spline = spline + ', на [' + str(x[j]) + ';' + str(x[j+1]) + ']'
    print(spline)
