n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
operacao = 0
while operacao != 5:
    print(
        '-=-=-=-=-MENU-=-=-=-=-\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n-=-=-=-=-=-=-=-=-=-=-=')
    operacao = int(input('Operação: '))
    if operacao == 1:
        print(f'\033[32mRESULTADO: {n1} + {n2} = {n1+n2}\033[m')
        print()
    elif operacao == 2:
        print(f'\033[32mRESULTADO: {n1} x {n2} = {n1*n2}\033[m')
        print()
    elif operacao == 3:
        print(f'\033[32mRESULTADO: {max(n1,n2)} é maior que {min(n1,n2)}.\033[m')
        print()
    elif operacao == 4:
        print()
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print()
    elif operacao == 5:
        print('Finalizando...')
    else:
        print('\033[31mOpção inválida\033[m')
print('-=-=-=-=-=-=-=-=-=-=-=\nFim do programa.')
