r1 = float(input('Escreva o comprimento de uma reta: '))
r2 = float(input('Escreva o comprimento de outra reta: '))
r3 = float  (input('Escreva o comprimento de outra reta: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('É possível formar um triângulo com essas retas.')
else:
    print('Não é possível formar um triângulo com essas retas.')