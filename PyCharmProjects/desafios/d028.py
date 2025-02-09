from random import randint
from time import sleep
num = randint(0,5)
print('\033[33m-=-\033[m'*20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar!\033[m')
print('\033[33m-=-\033[m'*20)
user_num = int(input('Em que número eu pensei?\033[32m \033[m'))
print('\033[35mPROCESSANDO...\033[m')
sleep(3)
if user_num == num:
    print('\033[32mPARABENS, você venceu! Eu pensei mesmo no número {}.\033[m'.format(num))
else:
    print('\033[31mPERDEU! Eu pensei no número {} e não no {}.\033[m'.format(num,user_num))