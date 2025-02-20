n = []
while True:
    n.append(int(input('Digite um valor: ')))
    r = input('Quer continuar? [S/N] ').upper().strip()[0]
    if r not in 'S':
        break
par = [v for v in n if v % 2 == 0]
impar = [v for v in n if v % 2 == 1]
print('-='*30)
print(f'A lista completa é {n}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')