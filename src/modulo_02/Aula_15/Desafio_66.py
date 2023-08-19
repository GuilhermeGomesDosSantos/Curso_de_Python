# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsidere o flag)

num = 0
numDigitados = 0
soma = 0

while True:
    num = int(input('Digite um Valor (999 para parar): '))

    if num == 999:
        break

    numDigitados += 1
    soma += num

print(f'A soma dos {numDigitados} valores foi {soma}!')