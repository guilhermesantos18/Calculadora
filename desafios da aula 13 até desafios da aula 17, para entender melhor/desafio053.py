frase = str(input('Digite uma frase para saber se é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    print('A palavra invertida fica {}'.format(inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo')
