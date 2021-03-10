print('-='*15)
print('Progressão aritmética')
print('-='*15)
num = int(input('Digite um valor: '))
razao = int(input('Digite a razão: '))
primeiro = num
cont = 1
total = 0
termos = 10
while termos != 0:
    total = termos + total
    while cont <= total:
        print('{} > '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('Pausa')
    termos = int(input('Quantos termos você quer mostrar mais? '))
print('Acabou!')
