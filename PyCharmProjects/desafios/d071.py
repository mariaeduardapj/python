print('='*35)
print('{:35}'.format('BANCO CEV'))
print('='*35)
valor = int(input('Que valor voce quer sacar? R$'))
if valor >= 50:
    print(f'Total de {valor//50} notas de R$50')
    if valor % 50 == 0:
        valor = 0
    else:
        valor = valor % 50
if valor >= 20:
    print(f'Total de {valor//20} notas de R$20')
    if valor % 20 == 0:
        valor = 0
    else:
        valor = valor % 20
if valor >= 10:
    print(f'Total de {valor//10} notas de R$10')
    if valor % 10 == 0:
        valor = 0
    else:
        valor = valor % 10
if valor >= 1:
    print(f'Total de {valor//1} notas de R$1')
print('='*35)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')