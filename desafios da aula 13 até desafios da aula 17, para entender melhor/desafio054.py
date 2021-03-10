from datetime import date
data = date.today().year
pessoasmais = 0
pessoasmenos = 0
for c in range(1, 8):
    datanasc = int(input('Digite a sua data de nascimento: '))
    anos = data - datanasc
    if anos >= 21:
        pessoasmais += 1
    else:
        pessoasmenos += 1
print('O total de pessoas maioes de idade é {}'.format(pessoasmais))
print('O total de pessoas menores de idade é {}'.format(pessoasmenos))
