num_ant = 0
num = 1
contador = 0
n = int(input('Quantos números da Sequência de Fibonacci você quer? '))
while contador < n:
    print(num_ant, end=' ')
    num_ant, num = num_ant + num, num_ant
    contador += 1



