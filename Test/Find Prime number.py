from math import sqrt
for i in range(2,100):
    prime = True
    for Factor in range(2,int(sqrt(i)+1)):
        if i % Factor is not 0:
            Factor += 1
        else:
            prime = False
            break
    if prime == True:
        print(i)