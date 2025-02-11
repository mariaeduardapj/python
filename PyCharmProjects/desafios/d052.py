from math import sqrt, trunc
num = int(input('Digite um número: '))
raiz = sqrt(num)
rain_int = trunc(raiz)
contagem = 0
for c in range(2,rain_int+1):
    if num % c == 0: # Divide o número de 2 até a porção inteira da raiz desse número, se nenhuma dividi-lô, ele é primo
        contagem = 1
if contagem == 0 and num>=2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')