i=int(input('PLZ input a positive integer:'))
Factor = 2
if i == 1 :
    p = 'Prime number!'
else:
    while Factor < i:
        if i % Factor is not 0:
            p = 'Prime number!'
            Factor += 1
        else:
            p = 'Not a Prime number!'
            print('Minimum factor =', Factor)
            break
print(p)


