listanum = []
sub = 1
listanum.append(int(input('Digite um numero: ')))
listanum.append(int(input('Digite outro numero: ')))
for num in listanum:
    sub *= num
print(sub)
