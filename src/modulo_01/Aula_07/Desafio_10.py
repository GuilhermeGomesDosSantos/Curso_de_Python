# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# considere, US$1,00 = R$3,27


carteira = float(input('Quanto dinheiro você tem na carteira ? R$: '))
dolarHoje = 4.78
media = carteira/dolarHoje
print('Com R${:.2f} você pode comprar: US${:.2f}'.format(carteira, media))
