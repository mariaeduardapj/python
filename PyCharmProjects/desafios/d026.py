frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes nessa frase.'.format(frase.count('A')))
print('Ela aparece pela primeira vez no caracter {}.'.format(frase.find('A') + 1))
print('E pela última vez no caracter {}.'.format(frase.rfind('A') + 1))
