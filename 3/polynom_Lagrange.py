
x = [0, 0.5, 1, 2, 3.5, 4, 6]
f = [-15.351, 1.396, 34.206, 82.917, 57.901, 98.128, 123.178]
d = len(x)

a = []
L = []

for j in range(d):
    p = 1
    s = ''
    for i in range(d):
        if i == j:
            continue
        else:
            p = p * (x[j] - x[i])
            s = s + '(x-' + str(x[i]) + ')'
    k = f[j]/p
    a.append(k)
    L.append(s)

print(a)
print(L)

polynom_string = 'f(x) = '
for i in range(d):
    polynom_string = polynom_string + str(a[i]) + '*' + L[i] + '+'
polynom_string = polynom_string[:-1].replace('+-','-')

print(polynom_string)