num = int(input('Digite um número: '))
divisivel = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[31m', end='')
        divisivel += 1
    else:
        print('\033[33m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num,divisivel))
if divisivel == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')