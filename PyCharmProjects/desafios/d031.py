dist = float(input('Qual é a distância da sua viagem em KM/h? '))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print('Preço da passagem: R${:.2f}'.format(preco))
