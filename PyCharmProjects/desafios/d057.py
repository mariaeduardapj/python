sexo = input('Sexo [M/F]: ').upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = input('\033[31mAtenção - A informação digitada é inválida. \nEscreva a letra correspondete ao seu sexo.\033[m \nSexo [M/F]: ').upper().strip()[0]
print(f'Ok! Usuário do sexo {sexo}.'.replace('M', 'masculino').replace('F','feminino'))

