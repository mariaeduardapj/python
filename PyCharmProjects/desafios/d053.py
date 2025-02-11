frase = input('Escreva uma frase: ')
f_maiusc = frase.upper()
f = f_maiusc.replace(' ','')
f_contrario = f[::-1]
print('O inverso de {} é {}'.format(f_maiusc,f_contrario))
if f == f_contrario:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo. ')
