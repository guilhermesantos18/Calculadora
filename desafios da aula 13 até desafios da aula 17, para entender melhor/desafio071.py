print('-'*30)
print('{:^30}'.format('NOVO BANCO'))
print('-'*30)
dinheiro = int(input('Qual o valor que desaja levantar? '))
notas = 50
totalnotas = 0
while True:
    if dinheiro >= notas:
        dinheiro -= notas
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Total de {totalnotas} notas de {notas}€')
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totalnotas = 0
        if dinheiro == 0:
            break
