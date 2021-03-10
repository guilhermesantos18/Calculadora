listatotal = []
listapar = []
listaimpar = []
while True:
    listatotal.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a digitar valores [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A lista completa é {listatotal}')
for valores in listatotal:
    if valores % 2 == 0:
        listapar.append(valores)
    else:
        listaimpar.append(valores)
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
