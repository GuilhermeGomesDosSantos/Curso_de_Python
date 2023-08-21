# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
#             0          1        2        3           4
#            -4         -3       -2       -1          -1
#Tuplas são imutáveis

# print(lanche)
# print(lanche[1])
# print(lanche[3])
# print(lanche[-2])
# print(lanche[1:3])
# print(lanche[:2])
# print(lanche[-3:])

# lanche[1] = 'Refri'
# print(lanche[1])#vai dar erro

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi para caramba!')

# print(len(lanche))

# for cont in range(0, len(lanche)):
#     # print(cont)
#     print(lanche[cont])
# print('Comi pra caramba!')

# for pos, comida in enumerate (lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!')

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')

# print(sorted(lanche))
# print(lanche)

# a = (2,5,4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c.count(5))
# print(c)
# print(c.index(8))
# print(c.index(2, 4))
# print(c.index(5, 1))

# pessoa = ('Guilherme', 20, 'M', 95.3)
# print(pessoa)
# del(pessoa)
# print(pessoa)

pessoa = ('Guilherme', 20, 'M', 95.3)
del(pessoa[0])#Não pode