print('-'*30)
print('{:^30}'.format('Lidl'))
print('-'*30)
total = produtosmais1000 = precomaisbarato = cont = 0
nomemaisbarato = ' '
while True:
    nome = str(input('Qual o nome do produto: '))
    preco = float(input('Qual o seu preço: € '))
    cont += 1
    total += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a comprar produtos [S/N]? ')).strip().upper()[0]
        if preco > 1000:
            produtosmais1000 += 1
        if cont == 1:
            nomemaisbarato = nome
            precomaisbarato = preco
        if preco < precomaisbarato:
            nomemaisbarato = nome
            precomaisbarato = preco
    if continuar == 'N':
        break
print(f'O total gasto no compra foi {total}€')
print(f'Existem {produtosmais1000} produtos que custam mais de 1000€')
print(f'O nome do produto mais barato é o/a {nomemaisbarato} e custa {precomaisbarato}€')
