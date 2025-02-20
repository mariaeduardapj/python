lista = []
e = input('Digite a expressão: ')
for c in e:
    if c == '(':
        lista.append('(')
    elif c ==  ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
