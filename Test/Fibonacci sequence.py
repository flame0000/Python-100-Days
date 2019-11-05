n=int(input('n ='))
a=1
b=1
print('1:',a)
print('2:',b)
for i in range(n-2):
    c=a+b
    print('%d:'%(i+3),c)
    a=b
    b=c