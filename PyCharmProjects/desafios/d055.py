pesos = [] # Lista vazia
for c in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    pesos.append(peso) # Preenche a lista a cada input
print(f'O menor peso lido foi de {min(pesos)}Kg')
print(f'O maior peso lido foi de {max(pesos)}Kg')