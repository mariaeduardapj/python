cidade = (input('Digite o nome de uma cidade: '))
dividido = cidade.upper().split()
print('O nome dessa cidade começa com Santo: {}'.format('SANTO' in dividido[0]))

# cid = str(input('Em que cidade você nasceu? ')).strip()
# print(cid[:5].upper() == 'SANTO')