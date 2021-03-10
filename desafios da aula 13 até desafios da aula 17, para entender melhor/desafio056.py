media = 0
pessoas = 0
idade1 = 0
nomemaisvelho = ' '
idademaisvelho = 0
mulheresanos20 = 0
for c in range(1, 5):
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual é a sua idade: '))
    sexo = str(input('Qual é o seu sexo [M/F]: ')).strip().upper()[0]
    pessoas += 1
    idade1 += idade
    if c == 1 and sexo in 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    elif idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
    elif sexo in 'F' and idade < 20:
        mulheresanos20 += 1
media = idade1 / pessoas
print('A média de idade do grupo é {}'.format(media))
print('O nome do homem mais velho no grupo é o {}'.format(nomemaisvelho))
print('A total de mulheres com menos de 20 anos é {}'.format(mulheresanos20))
