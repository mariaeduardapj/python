soma_idades = 0
mulheres = 0
maior_idade = 0
h_maisvelho = ''
for c in range(1,5):
    print('----- {}° PESSOA -----'.format(c))
    nome = input('Nome? ')
    idade = int(input('Idade? '))
    sexo = input('Sexo [M/F]: ').upper()
    soma_idades += idade
    if sexo == 'M' and idade > maior_idade:
        h_maisvelho = nome
        maior_idade = idade
    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1
print('A média de idade do grupo é de {:.1f} anos'.format(soma_idades/4))
print(f'O homem mais velho tem {maior_idade} anos e se chama {h_maisvelho}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos')


