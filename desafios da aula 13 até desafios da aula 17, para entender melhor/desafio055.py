pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input('Qual seu peso? kg'))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    elif peso > pesomaior:
        pesomaior = peso
    elif peso < pesomenor:
        pesomenor = peso
print('O maior peso digitado é {}kg'.format(pesomaior))
print('O menor peso digitado é {}kg'.format(pesomenor))
