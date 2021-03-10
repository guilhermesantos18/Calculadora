print('-='*15)
print('{:^10}'.format('Tente advinhar o meu número!'))
print('-='*15)
import random
computador = random.randint(0, 10)
jogador = palpites = 0
while jogador != computador:
    jogador = int(input('Digite um valor de 0 a 10: '))
    palpites += 1
    if jogador < computador:
        print('Está perto aumente mais')
    elif jogador > computador:
        print('Está perto diminua mais')
print('Você precisou de {} palpites para vencer!!!'.format(palpites))
print('Fim do jogo')
