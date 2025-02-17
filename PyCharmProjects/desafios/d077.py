palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGENS', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in palavras:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')

