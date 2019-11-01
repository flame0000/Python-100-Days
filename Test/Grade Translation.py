grade = int(input('PLZ input Grade:'))
if grade >=90 and grade <=100 :
    Level = 'A'
elif grade >= 80 :
    Level = 'B'
elif grade >= 70 :
    Level = 'C'
elif grade >= 60 :
    Level = 'D'
elif grade <= 60 and grade >=0 :
    Level = 'D'
else :
    Level = 'Not a grade'
print(Level)