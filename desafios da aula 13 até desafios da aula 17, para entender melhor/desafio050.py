soma = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
print('A soma de todos os valores digitados é {}'.format(soma))
