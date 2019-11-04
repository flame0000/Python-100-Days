a = int(input('PLZ input a positive integer:'))
b = int(input('PLZ input another positive integer:'))
if a >= b :
    Min = b
    Max = a
else :
    Min = a
    Max = b
for i in range(1,Min+1) :
    if a % i ==0 and b % i ==0 :
        divisor = i
multiple = a * b / divisor
print('Maximum common divisor = %d and least common multiple = %d' % (divisor,multiple))