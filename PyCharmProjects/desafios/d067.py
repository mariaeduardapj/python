while True:
    n = int(input('Digite um \033[34mnúmero\033[m para ver sua \033[34mtabuada\033[m ou \033[31m0\033[m para \033[31mencerrar\033[m o programa:\n'))
    print('-=-'*10)
    if n < 0:
        break
    print(f'TABUADA DO {n}')
    for c in range(1,11):
        print('{} x {:2} = {:2}'.format(n,c,n*c))
    print('-=-' * 10)
print('FIM DO PROGRAMA')