from random import randint
import emoji
import pygame
pygame.init()
pygame.mixer.init()
print('\033[35m=-'*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)
r = ''
p_i = ''
cont = 0
while True:
    jogador = int(input('\033[mDiga um valor: '))
    while p_i not in 'PI':
        p_i = input('Par ou Impar? [P/I] ').upper().strip()[0]
    pc = randint(0,10)
    if (jogador+pc) % 2 == 0:
        r = 'PAR'
        user_pi = 'P'
    else:
        r = 'ÍMPAR'
        user_pi = 'I'
    print('-' * 55)
    print(f'Você jogou {jogador} e o computador {pc}. Total de {jogador+pc} DEU {r}')
    print('-' * 55)
    if p_i == user_pi:
        pygame.mixer.music.load('C:/Users/duda2/Estudos/CursoemVideo/python/audiosd058/ganhou.mp3')
        pygame.mixer.music.play()
        cont += 1
        print(f'\033[32mVocê VENCEU {emoji.emojize(':party_popper:')} \nVamos jogar novamente...\033[m')
        print('=-' * 13)
    else:
        pygame.mixer.music.load('C:/Users/duda2/Estudos/CursoemVideo/python/audiosd058/perdeu.mp3')
        pygame.mixer.music.play()
        print('\033[31mVocê PERDEU!\033[m')
        print('=-' * 13)
        break
print(f'\033[1mFIM DO JOGO \nVocê venceu {cont} vezes.')
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)