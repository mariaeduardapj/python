matriz = [[0,0,0],[0,0,0],[0,0,0]]
c = s = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        if matriz[linha][coluna] % 2 == 0:
            s += matriz[linha][coluna]
        if coluna == 2:
            c += matriz[linha][coluna]
    print()
print()
print(f'A soma dos valores pares digitados é {s}.')
print(f'A soma dos valores da terceira coluna é {c}.')
print(f'O maior valor da segunda linha é {max(matriz[2])}.')