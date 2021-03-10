print()
print('{:-^40}'.format('Calculadora'))
print()
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
while True:
    print("""Escolha uma diz opções:\n
    Prima - [1] - Somar
    Prima - [2] - Subtrair
    Prima - [3] - Multiplicar
    Prima - [4] - Adicionar outro número
    Prima - [5] - Sair do programa\n""")
    opcao = int(input('Digite a sua opção pretendida: '))
    print()
    if opcao == 1:
        print('O resultado da soma entre {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado da subtração entre {} - {} = {}'.format(n1, n2, n1 - n2))
    elif opcao == 3:
        print('O resultado da multiplicação entre {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 4:
        n2 = int(input('Digite outro número inteiro: '))
    elif opcao == 5:
        break
print('{:-^40}'.format('Fim do programa volte sempre!'))
