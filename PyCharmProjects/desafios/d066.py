soma = cont = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'\033[36mVocê digitou {cont} números e a soma deles foi {soma}.')
