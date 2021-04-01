listanum = []
soma = subtracao = 0
# Interface
print('-' * 60)
print('Calculadora'.center(60))
print('-' * 60)
tiponumeros = str(input('Você deseja trabalhar com que tipos de números [inteiros, reais]? ')).lower().strip()
while True:
    if tiponumeros != 'inteiros':
        print(f'\033[31mA palavra que inseriu não existe, por favor digite novamente\033[m')
    elif tiponumeros == 'inteiros':
        # Leitura de dados
        listanum.append(int(input('Digite um número: ')))
        listanum.append(int(input('Digite outro número: ')))
        continuar = ' '
        if continuar not in 'SN':
            continuar = str(input('Quer continuar a digitar mais números [S/N]: ')).upper().strip()[0]
        if continuar == 'N':
            print('-' * 60)
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
                print('-' * 60)
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
                    mult = 1
                    for num in listanum:
                        mult *= num
                    print(f'O resultado é igual a \033[32m{mult}\033[m')
                elif opcao == 4:
                    div = 0
                    for num in listanum:
                        div /= num
                    print(f'O resultado é igual a \033[32m{div}\033[m')
    elif tiponumeros == 'reais':
        print('Ola, mundo')
