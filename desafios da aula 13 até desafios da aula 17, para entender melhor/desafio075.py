num = (int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')))
print(f'O número 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O número 3 encontrasse na posição {num.index(3)}')
else:
    print('O número 3 não foi localizado.')
print('Os números pares digitados foram ', end='')
for cont in num:
    if cont % 2 == 0:
        print(cont, end=' ')
