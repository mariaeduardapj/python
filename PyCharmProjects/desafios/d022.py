nome = (input('Digite seu nome completo: '))
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ',''))))
# print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0],len(dividido[0])))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))