from datetime import date
ano = int(input('Qual é o ano do seu nascimento? '))
if ano+18 > date.today().year:
    print('\033[34mAinda não chegou seu momento de se alistar, mas fique atento ao prazo!\033[m')
    print('Seu alistamento é em \033[1m{}\033[m. Falta(m) \033[1m{}\033[m ano(s).'.format(ano+18, ano+18-date.today().year))
elif ano+18 == date.today().year:
    print('\033[1;32mATENÇÃO JOVEM:\033[32m É hora de se ALISTAR para o SERVIÇO MILITAR!\033[m')
    print('O periodo de alistamento é de \033[1m1° de janeiro à 30 de julho de {}\033[m.'.format(date.today().year))
else:
    print('\033[31mO momento de se alistar já passou. Não se alistar acarreta em diversas proibições.\033[m')
    print('Mas você ainda pode se alistar comparecendo a Junta de Serviço Militar (JSM) \nmais próxima da sua residência e efetuando o pagamento da multa.')
    print('Você infrigiu o tempo em \033[1m{} ano(s)\033[m, portanto o valor da multa é de aproximadamente \033[1mR${}.\033[m '.format(date.today().year-(ano+18),(((date.today().year-(ano+18))*12)//3)*5.91))