num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + 1, razao):
    print(c, end=' > ')
print('Acabou!', end='')
