soma = cont = n1 = 0
n1 = int(input('Digite um valor [Digite 999 para parar o programa]: '))
while n1 != 999:
    cont += 1
    soma += n1
    n1 = int(input('Digite um valor [Digite 999 para parar o programa]: '))
print('O total de número digitados foi {} e a soma deles tudos é {}'.format(cont, soma))
