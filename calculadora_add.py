import math
while True:
    # Leitura de dados
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Quer continuar a digitar mais números: ')).upper().strip()