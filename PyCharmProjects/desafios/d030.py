num = int(input('\033[35mDigite um número:\033[32m \033[m'))
resultado = num % 2
#if resultado == 0 :
    #print('Esse número é par.')
#else:
    #print('Esse número é ímpar.')
print('{} é \033[34mPar\033[m'.format(num) if resultado==0 else '{} é \033[34mÍmpar\033[m'.format(num))