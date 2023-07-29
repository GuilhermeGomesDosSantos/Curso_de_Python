# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

num = int(input('Me dia um número qualquer: '))
if num % 2 == 0:
    print('O Número {} é PAR!'.format(num))
else:
    print('O Número {} é IMPAR!'.format(num))