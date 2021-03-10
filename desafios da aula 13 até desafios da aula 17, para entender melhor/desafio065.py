media = soma = cont = maior = menor = 0
continuar = ' '
while continuar != 'N':
    n1 = int(input('Digite um valor: '))
    cont += 1
    soma += n1
    continuar = str(input('Deseja continuar a digitar valores [S/N]: ')).strip().upper()[0]
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma / cont
print('A média de todos os valores digitados é {}'.format(media))
print('O maior valor lido foi {} e o menor foi {}'.format(maior, menor))
