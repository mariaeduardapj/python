numeros = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if not numeros or n > numeros [-1]:
        numeros.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(numeros) and n > numeros[pos]:
            pos += 1
        numeros.insert(pos,n)
        print(f'Adicionado na posição {pos} da lista.')
print('-='*20)
print(f'Os valores digitados foram {numeros}')

