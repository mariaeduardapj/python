peso = float(input('Qual seu peso? (Kg)  '))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura**2)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está em sobrepeso.')
elif 30 <= imc < 40:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade mórbida.')