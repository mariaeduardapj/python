soma = caros = preco_b = cont = 0
nome_b = ''
print('-'*44)
print('             LOJA SUPER BARATÃO')
print('-'*44)
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    soma += preco
    if preco > 1000:
        caros += 1
    if cont == 0 or preco<preco_b:
        preco_b = preco
        nome_b = produto
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print('{:-^44}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_b} que custa R${preco_b:.2f}')
