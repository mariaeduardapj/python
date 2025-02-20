n = []
while True:
    num = int(input('Digite um valor: '))
    continuar = input('Quer continuar? [S/N] ').upper().strip()
    n.append(num)
    if continuar not in 'S':
        break
print('-='*25)
print(f'Você digitou {len(n)} elementos.')
n.sort(reverse=True)
print(f'Os valores em ordem decrescente são {n}')
if 5 in n:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista')