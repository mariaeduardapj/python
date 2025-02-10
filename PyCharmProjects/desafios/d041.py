from datetime import date
ano = int(input('Em que ano o atleta nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('Classificaçõa: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')


