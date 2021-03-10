lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-'*40)
print('{:^40}'.format('Listagem de preços'))
print('-'*40)
c = 0
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'€{lista[c]:>7.2f}')
