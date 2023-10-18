C=int(input('Podaj wzorst w cm\n'))
#foot=30.48cm
#inch=2.54cm
foot=C//30
inch=(C-foot*30)//2.54
print(foot)
print(inch)