from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
maior = 0
n3 = 0
while n3 != 5:
    sleep(2)
    print('''Escolhe uma das seguintes opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior valor
    [4] Adicionar novos números
    [5] Sair do programa''')
    n3 = int(input('Digite a opção pretendida: '))
    if n3 == 1:
        print('A soma de {} + {} é {}'.format(n1, n2, n1 + n2))
    if n3 == 2:
        print('A multiplicação de {} x {} é {}'.format(n1, n2, n1*n2))
    if n3 == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor digitado foi {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior valor digitado foi {}'.format(maior))
    if n3 == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
sleep(2)
print('Encerrando... Volte sempre!')
