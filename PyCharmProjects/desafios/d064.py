num = contador = soma = 0
while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    if num != 999: soma += num
    if num != 999: contador += 1
print(f'Você digitou {contador} números e a soma deles foi de {soma}.')