n = []
while True:
    num = (int(input('Digite um valor: ')))
    if num in n:
        print('Valor duplicado! Não vou adicionar...')
    else:
        n.append(num)
        print('Valor adicionado com sucesso...')
    c = input('Quer continuar? [S/N] ').upper().strip()
    if c not in 'S':
        break
print('-='*30)
n.sort()
print(f'Você digitou os valores {n}')