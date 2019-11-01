from math import sqrt

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if c < a+b and c > abs(a-b):
    Perimeter = a + b + c
    p = Perimeter / 2
    Area = sqrt(p * (p-a) * (p-b) * (p-c))
    print('Perimeter = %.2f , Area = %.2f' % (Perimeter, Area))
else:
    print('Not a triangle!')