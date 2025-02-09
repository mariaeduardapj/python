salario = float(input('Qual é o salário do funcionário? R$\033[32m \033[m'))
aumento = salario+(salario*10/100) if salario>1250.00 else salario+(salario*15/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,aumento))
