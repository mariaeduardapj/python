dados = []
while True:
    nome =(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    dados.append([nome, [nota1, nota2]])
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r not in 'S':
        break
print('-='*30)
print(f'\033[1m{"No.":<5}{"NOME":<14}{"MÉDIA":>5}\033[m')
print('-'*24)
for c in range(0, len(dados)):
    print(f'{c+1:<5}', end='')
    print(f'{dados[c][0]:<14}', end='')
    print(f'{round((dados[c][1][0]+dados[c][1][1])/2, 1):>5}')
print('-'*48)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    elif 0 <= n-1 <= len(dados):
        print(f'\033[1mNotas de {dados[n-1][0]} são {dados[n-1][1]}\033[m')
        print('-'*48)
    else:
        print(f'\033[1mEste número não corresponde a nenhum aluno.\033[m ')
        print('-'*48)
print('\033[31mPROGRAMA FINALIZADO')