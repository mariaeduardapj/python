from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:\033[32m \033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[34mBISSEXTO\033[m.'.format(ano))
else:
    print('O ano {} \033[31mNÃO\033[m é \033[31mBISSEXTO\033[m.'.format(ano))