p =  int(input('Preço do produto - R$'))
n = p * 5 / 100
pn = p - n
print('Desconto de 5% aplicado!')
print('Seu produto sairá por R${}'.format(pn))