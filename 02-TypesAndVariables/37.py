I=str(input('Podaj imie\n'))
N=str(input('Podaj nazwisko\n'))
Y=int(input('Podaj rok urodzenia\n'))
M=str(int(input('Podaj miesiac urodzenia\n')))
D=int(input('Podaj dzien urodzenia\n'))
a=str(I[0])
b=str(N[0])
B=str(Y)+'-'+str(M)+'-'+str(D)
print('Name:', I)
print("Surname:", N)
print('Initials:', a+b)
print('Born:', B)