from random import randint
from time import sleep
import emoji
jogo = []
jogos = []
print('\033[32m-'*50)
print(f'{emoji.emojize('JOGO DA MEGA SENA :money_bag:'):^50}')
print('-'*50)
n = int(input('\033[mQuantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-=-= SORTEANDO {n} JOGOS =-=-=-=-=-')
for c in range(0,n):
    for p in range(0,6):
        j = randint(1,60)
        while j in jogo:
            j = randint(1,60)
        jogo.append(j)
    jogos.append(jogo[:])
    jogo.clear()
for j in range(0,n):
    sleep(1)
    print(f'Jogo {j+1}: {jogos[j]}')
print()
sleep(1)
print('\033[32mBOA SORTE!')
