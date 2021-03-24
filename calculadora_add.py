listanum = []
# Interface
print('-' * 50)
print('Calculadora'.center(50))
print('-' * 50)
while True:
    tiponumeros = str(input('Você deseja trabalhar com que tipos de números [inteiros, reias]? ')).lower().strip()
    if tiponumeros not in 'inteiros':
        print(f'\033[31mA palavra que inseriu não existe, por favor digite novamente\033[m')
    else:
        if tiponumeros == 'inteiros':
            while True:
                # Leitura de dados
                listanum.append(int(input('Digite um número: ')))
                listanum.append(int(input('Digite outro número: ')))
                continuar = ' '
                while continuar not in 'SN':
                    continuar = str(input('Quer continuar a digitar mais números [S/N]: ')).upper().strip()[0]
                if continuar == 'N':
                    break
            while True:
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
                    if opcao == 5:
                        break
                    elif opcao == 1:
                        print('Ola, mundo!')
                    elif opcao == 2:
                        pass
                    elif opcao == 3:
                        pass
                    elif opcao == 4:
                        pass
    print('Volte, sempre!')
# elif tiponumeros == 'reais':
