cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número ente 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número \033[1m{cont[n]}\033[m')
        print('-=-'*20)
        continuar = input('Você quer continuar? [S/N] ').upper().strip()
        if 'S' not in continuar:
            print('\033[31mFIM DO PROGRAM\033[m')
            break
    else:
        print('\033[31mNúmero inválido.\033[m ', end='' )

