print('-='*10)
print('{:^5}'.format('Análise de dados'))
print('-='*10)
mais18 = homens = mulheresmenos20 = 0
while True:
    idade = int(input('Qual sua idade: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a registar pessoas [S/N]: ')).strip().upper()[0]
        if idade > 18:
            mais18 += 1
        if sexo in 'M':
            homens += 1
        if sexo in 'F' and idade < 20:
            mulheresmenos20 += 1
    if continuar == 'N':
        break
print(f'O total de pessoas com 18 anos é {mais18}')
print(f'O total de homens cadastrados foi {homens}')
print(f'O total de mulheres cadastradas com menos de 20 menos é {mulheresmenos20}')
