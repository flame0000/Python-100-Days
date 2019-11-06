def Palindrome(num):
    fix = num
    temp = 0
    while num > 0:
        temp = temp * 10 + num % 10
        num //= 10
    return temp == fix

a = int(input('x = '))
print(Palindrome(a))