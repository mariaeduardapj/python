from random import randint
import emoji
from time import sleep

print('\033[31m-=-'*20)
print('{}JOKENPÔ COM O COMPUTADOR'.format(' '*18))
print('-=-'*20)

pc = randint(1,3) # Escolha do computador
nick = input('\033[35mNome de usuário:\033[m ')

# Opções
print(f'Escolha uma dos números abaixo:')
print(f'1 - Pedra {emoji.emojize(':right-facing_fist:')}')
print(f'2 - Papel {emoji.emojize(':page_facing_up:')}')
print(f'3 - Tesoura {emoji.emojize(':scissors:')}')

# Escolha do usuário
user = int(input(f'\033[35m{nick}:\033[m '))

# Dicionário
opcoes = {1: '🤜', 2: '📄', 3: '✂️'}

# Imprime escolhas
print(f'{nick} {opcoes.get(user, "?")} \n🆚')
sleep(1)
print(f'Computador {opcoes.get(pc, "?")}')
sleep(1)
print('\033[31m-=-\033[m'*20)

# Determina o resultado
if pc==1 and user==1 or pc==2 and user==2 or pc==3 and user==3:
    print('\033[33mEMPATE\033[m')
elif pc==1 and user==3 or pc==2 and user==1 or pc==3 and user==2:
    print('\033[31mVOCÊ PERDEU!\033[m')
else:
    print('\033[32mVOCÊ VENCEU!\033[m')
