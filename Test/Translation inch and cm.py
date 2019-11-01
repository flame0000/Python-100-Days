value=float(input('PLZ input value:'))
unit=input('PLZ input unit:("in" or "cm")')
print(value, unit)
if unit == 'cm':
    output = value / 2.54
    print('%.2f cm = %.2f in' % (value, output))
elif unit == 'in':
    output = value * 2.54
    print('%.2f in = %.2f cm' % (value, output))
else:
    print('PLZ check unit!')
