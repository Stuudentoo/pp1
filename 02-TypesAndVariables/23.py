import math
a=int(input('Długość pierwszego boku\n'))
b=int(input('Długość drugiego boku\n'))
c=int(input('Długość trzeciego boku\n'))
O=a+b+c
print('Triangle circumference:',O)
P=(O/2)*((O/2)-a)*((O/2)-b)*((O/2)-c)
p=math.sqrt(P)
print('Triangle area:',p)