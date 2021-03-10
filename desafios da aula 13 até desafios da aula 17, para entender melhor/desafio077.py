lista = ('carro', 'python', 'fixe', 'mota', 'netflix', 'automacao')
for palavra in lista:
        print(f'\nNa palavra {palavra.upper()} temos ', end='')
        for letra in palavra:
            if letra.lower() in 'aeiou':
                print(f'{letra}', end=' ')

