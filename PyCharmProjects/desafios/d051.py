a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0,10):
    print('{}'.format(a1+(r*c)), end=' ⭢ '  )
print('FIM')
