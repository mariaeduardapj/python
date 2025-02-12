from random import randint
from time import sleep
import emoji
import pygame
pygame.init()
pygame.mixer.init()
user_num = 11
contador = 0

print('\033[35m-=-\033[m'*20)
print('\033[34mVou pensar em um número entre 0 e 10. Tente adivinhar!\033[m')
print('\033[35m-=-\033[m'*20)
pc_num = randint(0, 10)

while user_num != pc_num:
    user_num = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1.5)
    contador += 1

    if user_num != pc_num:
        pygame.mixer.music.load('C:/Users/duda2/Estudos/CursoemVideo/python/audiosd058/perdeu.mp3')
        pygame.mixer.music.play()
        if pc_num < user_num:
            m = 'menor'
        else:
            m = 'maior'
        print(f'\033[31mPERDEU! Eu pensei num número {m} que {user_num}.\033[m\nTente novamente! ', end='')

pygame.mixer.music.load('C:/Users/duda2/Estudos/CursoemVideo/python/audiosd058/ganhou.mp3')
pygame.mixer.music.play()
print(f'\033[32mPARABENS{emoji.emojize(':party_popper:')} você venceu! Eu pensei mesmo no número {user_num}.\033[m')
print(f'\033[3mNúmero de tentativas - {contador}')

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)