matriz = []
u = y = s =0
for m in range(0,9):
    n = int(input(f'Digite um valor para [{y},{u}]: '))
    matriz.append(n)
    u += 1
    if u > 2:
        u = 0
        y += 1
print('-='*30)
print(f'[  {matriz[0]}  ][  {matriz[1]}  ][  {matriz[2]}  ]')
print(f'[  {matriz[3]}  ][  {matriz[4]}  ][  {matriz[5]}  ]')
print(f'[  {matriz[6]}  ][  {matriz[7]}  ][  {matriz[8]}  ]')
for p in matriz:
    if p % 2 == 0:
        s += p
print()
print(f'A soma dos valores pares digitados é {s}.')
print(f'A soma dos valores da terceira coluna é {matriz[2]+matriz[5]+matriz[8]}.')
print(f'O maior valor da segunda linha é {max(matriz[3:6])}.')
