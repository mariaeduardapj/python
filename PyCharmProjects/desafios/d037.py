print('\033[35m========== CONVERSOR DE BASES NÚMERICAS ==========\033[m')
num = int(input('Digite um número inteiro: '))
print('1 - Binário \n2 - Octal \n3 - Hexadecimal')
base = int(input('Escolha uma Base para Conversão: '))
if base == 1:
    print('\033[35m{}\033[m convertido para \033[35mbinário\033[m é igual a \033[1;35m{}\033[m'.format(num, bin(num)[2:])) # Converte Decimal para Binário
elif base == 2:
    print('\033[35m{}\033[m convertido para \033[35moctal\033[m é igual a \033[1;35m{}\033[m'.format(num, oct(num)[2:])) # Converte Decimal para Octal
elif base == 3:
    print('\033[35m{}\033[m convertido para \033[35mhexadecimal\033[m é igual a \033[1;35m{}\033[m'.format(num, hex(num)[2:])) # Converte Decima para Hexadecimal
else:
    print('O valor que você digitou não é uma das opções acima.')
