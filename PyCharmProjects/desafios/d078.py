n = []
for c in range(0,5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
pmenor = [i for i, valor in enumerate(n) if valor == min(n)] # Para cada ÍNDICE i em que o VALOR v  for igual ao menor valor da LISTA n adicione o indice na LISTA menor
pmaior = [i for i, valor in enumerate(n) if valor == max(n)]
print(f'Você digitou os valores {n}')
print(f'O menor valor digitado foi {min(n)} na posição {pmenor}.')
print(f'O maior valor digitado foi {max(n)} na posição {pmaior}.')
