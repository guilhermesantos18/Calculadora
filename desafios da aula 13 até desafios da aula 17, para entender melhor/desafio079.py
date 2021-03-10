lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a adcionar valores há lista [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
lista.sort()
print(f'Você digitou os valores {lista}')
