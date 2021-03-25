listanum = []
listanum.append(int(input('Digite um numero: ')))
listanum.append(int(input('Digite outro numero: ')))
numsub = listanum[0]
print(numsub)
for num in listanum:
    print(num)
    numsub -= num
print(numsub)
