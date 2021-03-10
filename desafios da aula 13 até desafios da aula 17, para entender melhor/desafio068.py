print('-='*15)
print('Vamos jogar ao PAR OU ÍMPAR')
print('-='*15)
from random import randint
vitorias = 0
par = 'PAR'
impar = 'IMPAR'
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 10)
    soma = jogador + computador
    possibilidades = str(input('Quer [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ', end='')
    if soma % 2 == 0:
        print(f'{par}')
    if soma % 2 == 1:
        print(f'{impar}')
    if possibilidades == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
            print('-='*15)
        else:
            print('Você PERDEU!')
            break
    elif possibilidades == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
            print('-='*15)
        else:
            print('Você PERDEU!')
            break
print('-='*15)
print(f'GAME OVER! Você venceu {vitorias} vezes')
