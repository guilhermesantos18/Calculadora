while True:
    # Leitura de dados
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar a digitar mais números [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
while True:
    print('''Escolha uma das seguintes opções:
    Prima - [1] - Somar
    Prima - [2] - Subtrair
    Prima - [3] - Multiplicar
    ''')
    opcao = int(input('Digite a sua opção aqui: '))
    if opcao == 5:
        break
print('Volte sempre!')
