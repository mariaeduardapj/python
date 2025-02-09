nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m' , nome , '\033[m'))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))
