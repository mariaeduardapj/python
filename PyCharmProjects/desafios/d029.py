print('ATENÇÃO! Você está numa via cujo limite de velocidade é 80KM/H')
kmh = float(input('Qual a sua velocidade? '))
if kmh>80:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((kmh-80)*7))
print('Tenha um bom dia! Dirija com segurança!')