num = int(input('Digite um número: '))
resultado = num % 2
#if resultado == 0 :
    #print('Esse número é par.')
#else:
    #print('Esse número é ímpar.')
print('{} é Par'.format(num) if resultado==0 else '{} é Ímpar'.format(num))