'''
from Prime_num_F import pri
from Palindrome_number_judgement_F import Palindrome

if __name__ == '__main__':
    num = int(input('x = '))
    print(Palindrome(num) == True and pri(num) == True)
'''

import Prime_num_F
import Palindrome_number_judgement_F

if __name__ == '__main__':
    num = int(input('x = '))
    print(Palindrome_number_judgement_F.Palindrome(num) == True and Prime_num_F.pri(num) == True)