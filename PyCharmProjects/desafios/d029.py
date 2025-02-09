print('ATENÇÃO! Você está numa via cujo limite de velocidade é 80KM/H')
kmh = float(input('Qual a sua velocidade?\033[32m \033[m'))
if kmh>80:
    print('\033[31mMULTADO! Você excedeu o limite permitido de 80Km/h')
    print('Você deve pagar uma multa de \033[33mR${:.2f}\033[m'.format((kmh-80)*7))
print('\033[36mTenha um bom dia! Dirija com segurança!')