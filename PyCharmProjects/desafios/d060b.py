num = int(input('Digite um número: '))
_n = num
f = 1
print(f'\033[36m{num}!\033[m = ',end='')
while _n > 0:
    print('{} '.format(_n),end='')
    print('x ' if _n > 1 else ' = ', end='')
    f *= _n
    _n -= 1
print(f'\033[33m{f}')