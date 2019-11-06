def divisor(a,b):
    if a > b:
        a,b = b,a
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            d = i
    return d

def multiple(a,b):
    return a * b / divisor(a,b)

if __name__ == '__main__':
    if __name__ == '__main__':
        i = int(input('a = '))
        j = int(input('b = '))
        print('Maximum common divisor = %d and least common multiple = %d' % (divisor(i,j),multiple(i,j)))