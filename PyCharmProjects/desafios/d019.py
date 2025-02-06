import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do segundo aluno: ')
a4 = input('Nome do quarto aluno: ')

sorteio = random.choice([a1,a2,a3,a4])
print('O(A) aluno(a) sorteado(a) é {}'.format(sorteio))