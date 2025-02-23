galera = []
dado = []
menor = maior = 0
for c in range(0,5):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior+=1
    else:
        print(f'{p[0]} é menor de idade.')
        menor+=1
print(f'Temos {menor} menores e {maior} maiores de idade.')