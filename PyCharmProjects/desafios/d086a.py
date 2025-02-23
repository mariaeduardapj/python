matriz = []
u = y = 0
for m in range(0,9):
    n = int(input(f'Digite um valor para [{y},{u}]: '))
    matriz.append(n)
    u += 1
    if u > 2:
        u = 0
        y += 1
print('-='*30)
print(f'[ {matriz[0]} ][ {matriz[1]} ][ {matriz[2]} ]')
print(f'[ {matriz[3]} ][ {matriz[4]} ][ {matriz[5]} ]')
print(f'[ {matriz[6]} ][ {matriz[7]} ][ {matriz[8]} ]')

