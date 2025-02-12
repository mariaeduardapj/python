c = 'S'
soma = 0
contador = 0
valores = []
while c == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    contador += 1
    valores.append(n)
    c = input('Quer continuar? ').upper()
print('Você digitou {} números e a média foi {:.2f}. \nO menor valor foi {} e o maior {}.'.format(contador,soma/contador,min(valores),max(valores)))

