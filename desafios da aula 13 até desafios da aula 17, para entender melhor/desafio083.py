expressao = (str(input('Digite um expressão matemática:')))
cont1 = 0
cont2 = 0
for simb in expressao:
    if simb == '(':
        cont1 += 1
    if simb == ')':
        cont2 += 1
if cont1 == cont2:
    print('A expressão matemática está correta!')
else:
    print('A expressão matemática está incorreta')
