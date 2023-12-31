# Elabore um programa que calcule o valor a ser pago por um produto,
# consiferando o seu preço normal e condição de pagamento:
# -à vista dinheiro/cheque: 10% de desconto
# -à vista no cartão: 5% de desconto
# -em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros
# -à vista no cartão: 5% de desconto

print('{:=^40}'.format('LOJAS GD$'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 0.1)
    print('Sua compra de R${:.2f} vai custar: R${:.2f} no final'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar: R${:.2f} no final'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.2)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente Novamente')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))