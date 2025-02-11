from datetime import date
menores = 0
maiores = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if ano + 21 > date.today().year:
        menores += 1
    else:
        maiores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade, e {menores} pessoas menores de idade.')


