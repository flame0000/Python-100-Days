from math import sqrt
def pri(a):
    for i in range(2,int(sqrt(a))):
        if a % i == 0:
            return False
    if a != 1:
        return True
    else:
        return False

x = int(input('x = '))
print(pri(x))