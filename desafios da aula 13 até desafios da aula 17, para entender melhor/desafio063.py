termos = int(input('Digite a quantidade de termos da Sequência de Fibonnaci você quer: '))
n1 = 0
n2 = 1
print('{} > {} '.format(n1, n2), end='')
cont = 3
while cont <= termos:
    n3 = n1 + n2
    print('> {}'.format(n3).format(n3), end=' ')
    n1 = n2
    n2 = n3
    cont += 1
print('> Fim')
