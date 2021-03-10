soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('No total existem {} números ímpares e divisiveis por 3 e a soma deles todos é {}'.format(cont, soma))
