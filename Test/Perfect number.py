from math import sqrt
for i in range(1,100001):
    Sum = 0
    for j in range(1,int(i/2+1)):
        if (i % j) == 0:
            Sum += j
    if Sum == i:
        print(i)