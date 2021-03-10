extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print('Tente novamente. ', end='')
        continuar = ''
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar a digitar valores [S/N]: ')).strip().upper()[0]
        if continuar == 'N':
            break
        print(f'O número digitado escrito por extenso é {extenso[num]}')
