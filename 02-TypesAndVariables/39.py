Normal=float(input('Podaj pierwotna cene\n'))
N=round(Normal, 2)
Przecena=float(input('Podaj przecene w procentach\n'))
p=Przecena/100
P=round(p, 2)
After=N*P
A=round(After, 2)
Reduction=N-A
print(N)
print(P)
print(A)
print(round(Reduction, 2))