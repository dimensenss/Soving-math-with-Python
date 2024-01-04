from gaussMethod import Gauss

x = [0, 0.5, 1, 2, 3.5, 4, 6]
f = [-15.351, 1.396, 34.206, 82.917, 57.901, 98.128, 123.178]
d = len(x)
A = []

for j in range(d):
    s = []
    for i in range(d-1, -1, -1):
        s.append(x[j]**i)
    A.append(s)

for j in range(d):
    print(A[j])

c = Gauss(A,f)
print(c)

polynom_string = 'f(x) = '
for i in range(d):
    polynom_string = polynom_string + str(c[i]) + '*x^' + str(d-i-1) + '+'
polynom_string = polynom_string[:-5].replace('+-','-').replace('x^1', 'x')

print("\nІнтерполяційний поліном\n",polynom_string)