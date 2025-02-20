num = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N] ').upper().strip()
    num.append(n)
    if continuar not in 'S':
        break
for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')