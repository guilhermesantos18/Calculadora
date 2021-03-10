lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'O valor foi adicionado na {pos}ª posição')
                break
            pos += 1
print(f'A lista por ordem crescente fica {lista}')
