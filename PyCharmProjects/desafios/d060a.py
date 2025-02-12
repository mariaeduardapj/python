from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print(f'\033[36m{num}!\033[m = ',end='')
for c in range(num,0,-1):
    print(c,end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
print(f'\033[33m{f}')
