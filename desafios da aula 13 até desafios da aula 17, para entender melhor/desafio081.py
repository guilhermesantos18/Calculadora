lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a digitar valores [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'No total foram digitados {cont} números')
lista.sort(reverse=True)
print(f'A lista de valores de ordem decrescente fica da seguinte forma {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O número 5 não foi encontrado na lista.')
