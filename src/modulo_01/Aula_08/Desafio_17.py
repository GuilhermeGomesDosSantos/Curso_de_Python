# Faça um programa que leia o comprimento do cateto oposto e do cateto ajacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenisa

# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adiacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

# import math
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))