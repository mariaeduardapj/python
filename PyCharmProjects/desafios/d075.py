n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 está na {n.index(3)+1}° posição.')
else:
    print('O número 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')





