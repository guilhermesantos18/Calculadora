valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print('-='*25)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos, val in enumerate(valores):
    if val == max(valores):
        print(f'{pos}...', end=' ')
print(f'\nO menor valores digitado foi {min(valores)} nas posições ', end='')
for pos, val in enumerate(valores):
    if val == min(valores):
        print(f'{pos}...', end=' ')
