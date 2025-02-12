menor_18 = homens = mulheres_n = 0
print('-'*25)
print('   CADASTRE UMA PESSOA   ')
while True:
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade >= 18:
        menor_18 += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_n += 1
    print('-' * 25)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print(f'{menor_18} pessoas são maiores de idade.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres_n} mulheres menores de 20 anos foram cadastradas.')