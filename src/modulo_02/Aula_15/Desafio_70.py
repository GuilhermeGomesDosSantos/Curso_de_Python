# Crie um program aque leia o nome e o proço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre:
# A)Qual é o total gasto na compra
# B)Quantos produtos custam mais de R$1000
# C)Qual é o nome do produto mais barato

total = 0
produtoMaisMil = 0
produtoMaisBarato = ''
menorPreco = 0
cont = 0

print('-'*30)
print('LOJA SUPER BARATÂO')
print('-'*30)

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$: '))

    cont += 1
    total += preco

    if preco > 1000:
        produtoMaisMil += 1

    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = produto
    # else:
    #     if preco < menorPreco:
    #         menorPreco = preco
    #         produtoMaisBarato = produto

    res = ' '
    while res not in "SN":
        res = str(input("Quer continuar ? [S/N] ")).strip().upper()[0]

    if res != "S":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total de compra(s) foi R$:{total:10.2f}")
print(f"Temos {produtoMaisMil} produto(s) custando mais de R$1.000.00")
print(f"O produto mais barato foi {produtoMaisBarato} que custa R$:{menorPreco}")
