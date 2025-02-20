numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        print('Valor adicionado com sucesso!')
        numeros.append(n)
    else:
        print('Valor duplicado, não será adicionado.')
    continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar not in 'S':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')