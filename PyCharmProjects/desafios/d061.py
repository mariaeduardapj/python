a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = 0
pa = a1
print(pa,end=' ⭢ ')
while termos != 10:
    termos += 1
    pa += r
    print(pa,end=' ⭢ ')
print('FIM')