from random import randint
from time import sleep
num = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-'*20)
user_num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if user_num == num:
    print('PARABENS! Você venceu! \nEu pensei mesmo no número {}.'.format(num))
else:
    print('GANHEI! \nEu pensei no número {}, e não no {}.'.format(num,user_num))