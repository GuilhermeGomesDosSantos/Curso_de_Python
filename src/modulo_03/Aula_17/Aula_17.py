num = [2, 5, 9, 1]
num[2] = 3
#num[4] = 7 # Vai dar erro pois essa posição não existe na lista
num.append(7)
# num.sort()
# num.sort(reverse=True)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')
# num.insert(2, 0)
num.insert(2, 2)
# num.pop()
# num.pop(2)
# num.remove(2)

# if 4 in num:
#     num.remove(4)
# else:
#     print('Não achei o número 4')


# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 5')

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for v in valores:
#     print(f'{v}...', end='')

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!' )
# print('Cheguei ao final da lista')
# print(valores)

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Chegeui ao da lista')

a = [2,3,4,7]
b = a
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
