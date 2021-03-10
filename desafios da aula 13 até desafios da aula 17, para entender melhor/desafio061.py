print('-='*15)
print('Progressão aritmética')
print('-='*15)
num = int(input('Digite um valor: '))
razao = int(input('Digite a razão: '))
decimo = num + 10 * razao
while num != decimo:
    print(num, end=' > ')
    num += razao
print('Acabou!')
