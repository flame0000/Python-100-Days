l = int(input('PLZ input length of triangle:'))
for i in range(l+1) :
    print('*'*i)
for i in range(l + 1):
    print(' '*(l-i),'*' * i)
for i in range(l + 1):
    print(' ' * (l - i), '*' * (2 * i - 1))