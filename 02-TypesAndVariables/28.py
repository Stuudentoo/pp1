w=float(input('Podaj swoja wage w kilogramach\n'))
h=float(input('Podaj swoj wzrost w metrack\n'))
B=w/h**2
c=B//1
b=f'Your BMI index is {c}'
print(b)
if (24<c<29):
    print('True')
else:
    print('False')