preco_normal = float(input('Qual o preço do produto? R$ '))
print('-'*50)
print('''FORMAS DE PAGAMENTO:
1 - À vista no \033[34mdinheiro/cheque\033[m com \033[33m10%\033[m de desconto. 
2 - À vista no \033[34mcartão\033[m com \033[33m5%\033[m de desconto. 
3 - Em até \033[34m2x no cartão\033[m sem juros. 
4 - \033[34m3x ou mais no cartão\033[m com \033[33m20%\033[m de juros.''')
print('-'*50)

opcao = int(input('Escolha uma opção de pagamento: '))
if opcao == 1:
    print('\033[32mSua compra de R${:.2f} vai custar R${:.2f}.'.format(preco_normal, preco_normal-(preco_normal*10/100)))
elif opcao == 2:
    print('\033[32mSua compra de R${:.2f} vai custar R${:.2f}.'.format(preco_normal,preco_normal-(preco_normal*5/100)))
elif opcao == 3:
    print('\033[32mSua compra será parcelada em 2x de R${:.2f} sem juros.'.format(preco_normal/2))
    print('Sua compra vai custar R${:.2f} no final'.format(preco_normal))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print('\033[32mSua compra será parcelada em {}x de R${:.2f} com juros'.format(parcelas, (preco_normal+(preco_normal*20/100))/parcelas))
    print('Sua compra de R${:.2f} vai custar R${:2f}.'.format(preco_normal,preco_normal+(preco_normal*20/100)))
else:
    print('\033[31mO valor digitado não é uma das opções acima.')