cores = {'limpa':'\033[m',
         'violeta':'\033[35m',
         'verde':'\033[32m',
         'vermelhob':'\033[1;31m',
         'vermelhon':'\033[0;31m'}
r1 = float(input('{}Escreva o comprimento de uma reta: '.format(cores['violeta'])))
r2 = float(input('Escreva o comprimento de outra reta: '))
r3 = float  (input('Escreva o comprimento de outra reta: {}'.format(cores['limpa'])))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('{}É possível formar um triângulo com essas retas.{}'.format(cores['verde'],cores['limpa']))
else:
    print('{}Não{} é possível formar um triângulo com essas retas.{}'.format(cores['vermelhob'],cores['vermelhon'],cores['limpa']))