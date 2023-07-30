# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anosFinanciamento = int(input('Quantos anos de financiamento? '))

prestacaoMensal = valor / (anosFinanciamento * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anosFinanciamento))
print('a prestação será de R${:.2f}'.format(prestacaoMensal))
if prestacaoMensal <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')