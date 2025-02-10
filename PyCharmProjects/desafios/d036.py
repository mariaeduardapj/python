from time import sleep
print('\033[32m==========CONSULTA DE EMPRÉSTIMO BANCÁRIO==========\033[m')
sleep(1)
valor_casa = float(input('Qual o valor da casa? R$'))
salario =  float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos  de financiamento? '))
prestacao = (valor_casa / anos) / 12
p_salario = salario*30/100
print('\033[32m=\033[m'*51)
sleep(1)
print('Valor da prestação mensal: R${:.2f}'.format(prestacao))
sleep(1)
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
if prestacao <= p_salario:
    print('\033[1;34mEmpréstimo bancário APROVADO\033[m')
else:
    print('\033[1;31mEmpréstimo bancário NEGADO\033[m')
