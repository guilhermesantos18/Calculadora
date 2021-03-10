n1 = int(input('Digite um valor para mostrar o seu fatorial: '))
soma = 1
num = n1
while num > 0:
        print('{}'.format(num), end='')
        print(' x ' if num > 1 else ' = ', end='')
        soma *= num
        num -= 1
print('{}'.format(soma))
