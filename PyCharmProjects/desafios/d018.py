from math import radians, sin, cos, tan
angulo = float(input('Digite um Ângulo: '))
ang = radians(angulo) # Converte de ângulo para gradiano
print('Para o ângulo {}°'.format(angulo))
print('Seno {:.3f} \nCosseno {:.3f} \nTangente {:.3f}'.format(sin(ang),cos(ang),tan(ang)))