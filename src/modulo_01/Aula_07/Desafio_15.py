# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0.15 por Km rodado

km = float(input('Qual é a quantidade de Km percorrido pelo Carro ? '))
dias = int(input('por quantos dias o carro foi alugado ? '))
precoPagar = (dias * 60) + (km * 0.15)

print('O Total a pagar é: {:.2f}'.format(precoPagar))