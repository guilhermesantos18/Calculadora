listanum = []
soma = subtracao = multiplicacao = 0
# Interface
print('-' * 50)
print('Calculadora'.center(50))
print('-' * 50)
while True:
    tiponumeros = str(input('Você deseja trabalhar com que tipos de números [inteiros, reias]? ')).lower().strip()
    if tiponumeros not in 'inteiros' or tiponumeros == '':
        print(f'\033[31mA palavra que inseriu não existe, por favor digite novamente\033[m')
    elif tiponumeros == 'inteiros':
        # Leitura de dados
        listanum.append(int(input('Digite um número: ')))
        listanum.append(int(input('Digite outro número: ')))
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar a digitar mais números [S/N]: ')).upper().strip()[0]
        if continuar == 'N':
            break
while True:
    print('-' * 50)
    print('''Escolha uma das seguintes opções:
[1] - Somar
[2] - Subtrair
[3] - Multiplicar
[4] - Divisão
[5] - Sair do programa''')
    try:
        opcao = int(input('Digite o sua opção: '))
    except:
        print('\033[1;31mErro digite um número inteiro!\033[m')
    else:
        print('-' * 50)
        if opcao == 5:
            break
        elif opcao == 1:
            for num in listanum:
                soma += num
            print(f'O resultado é igual a \033[32m{soma}\033[m')
        elif opcao == 2:
            for num in listanum:
                subtracao -= num
            print(f'O resultado é igual a \033[32m{subtracao}\033[m')
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
# elif tiponumeros == 'reais':
