# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Qual é o Preço do produto? R$: '))
desconto = preco - (preco * 0.05)
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preco, desconto))
