
x = [0, 0.5, 1, 2, 3.5, 4, 6]
f = [-15.351, 1.396, 34.206, 82.917, 57.901, 98.128, 123.178]
d = len(x)
A = []

for j in range(d-1, -1, -1):
    s = [1]
    p = 1
    for i in range(j):
        p = p * (x[j] - x[i])
        s.append(p)
    s.reverse()
    A.append(s)

for i in range(d):
    print(A[i])

def scalar_product(A, f, n):
    s = 0
    r = len(A[n])
    for i in range(1, r-1):
        s = s + f[i]*A[n][r-i-1]
    return s

for i in range(1, d):
    f[i] = (f[i] - f[0] - scalar_product(A, f, d-i-1))/A[d-i-1][0]

print(f)

polynom_string = 'f(x) = ' + str(f[0]) + '+'
p = '*(x-' + str(x[0]) + ')'
for i in range(1, d):
    polynom_string = polynom_string + str(f[i]) + p + '+'
    p = p + '*(x-' + str(x[i]) + ')'
polynom_string = polynom_string[:-1].replace('+-','-')

print(polynom_string)