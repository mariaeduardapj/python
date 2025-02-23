dados = []
pesados = []
leves =[]

while True:
    nomes = str(input('Nome: '))
    pesos = float(input('Peso: '))
    dados.append([nomes,pesos])
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r not in 'S':
        break
maiorpeso = menorpeso = 0
for p in dados:
    if p[1] > maiorpeso:
        maiorpeso = p[1]
        pesados.clear()
        pesados.append(p[0])
    elif p[1] < menorpeso:
        menorpeso = p[1]
        leves.clear()
        leves.append(p[0])
    elif p[1] == maiorpeso:
        pesados.append(p[0])
    elif p[1] == menorpeso:
        leves.append(p[0])

print('-='*30)
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi {maiorpeso} Kg. Peso de {pesados}')
print(f'O menor peso foi {menorpeso}Kg. Peso de {leves}')

