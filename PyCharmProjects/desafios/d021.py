import pygame
pygame.init()
pygame.mixer.init()

audios = {
    '1': 'C:/Users/duda2/Estudos/CursoemVideo/python/audiosd021/audio1.mp3',
    '2': 'C:/Users/duda2/Estudos/CursoemVideo/python/audiosd021/audio2.mp3',
    '3': 'C:/Users/duda2/Estudos/CursoemVideo/python/audiosd021/audio3.mp3'
}

print('1 - Gusttavo Lima - Diz Pra Mim \n2 - Ludmilla - Falta de Mim (feat. Mari Fernandez) \n3 - Resenha do Arroxha - J. Eskine')
escolha = (input('Escolha um dos números para tocar a música: '))

if escolha in audios:
    pygame.mixer.music.load(audios[escolha])
    pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

else:
    print('Escolha inválida')
