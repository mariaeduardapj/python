a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = 0
mais = 10
print(a1,end=' ⭢ ')
while mais != 0:
    while termos != mais:
        termos += 1
        a1 += r
        print(a1,end=' ⭢ ')
    print('PAUSA')
    termos = 0
    mais = int(input('Quantos termos mais você quer ver? '))
print('Fim do programa.')
