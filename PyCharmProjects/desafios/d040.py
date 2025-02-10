nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print('\033[31mALUNO REPROVADO\033[m')
elif 5.0 <= media < 7:
    print('\033[33mALUNO DE RECUPERAÇÃO\033[m')
else:
    print('\033[32mALUNO APROVADO\033[m')