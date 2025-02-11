import pygame
import emoji
from time import sleep
pygame.init()
pygame.mixer.init()
print('\033[35m-=-=-=-=-CONTAGEM REGRESSIVA PARA OS FOGOS-=-=-=-=-')
for c in range(10,-1,-1):
    print(c)
    sleep(1)
for c in range(0,3):
    print(f'{emoji.emojize(':fireworks:'*23)}')
    pygame.mixer_music.load('C:/Users/duda2/Estudos/CursoemVideo/python/audiod045/firework _sound.mp3')
    pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
