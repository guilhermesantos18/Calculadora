while True:
    num = int(input('Digite um valor para saber a sua tabuada [Digite um número negativo para terminar]: '))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
print('Acabou!')
