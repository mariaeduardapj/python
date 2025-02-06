s = int(input('Salário atual - R$'))
n =  s * 15 / 100
sn = s + n
print('Seu salário recebeu um aumento de 15%, seu novo salário é de R${:.0f}'.format(sn))