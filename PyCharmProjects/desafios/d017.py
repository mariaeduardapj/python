from math import sqrt
co = int(input('Cateto oposto: '))
ca = int(input('Cateto adjacente: '))
h = sqrt(co**2 + ca**2)
print('O valor da hipotenusa é {}'.format(h))