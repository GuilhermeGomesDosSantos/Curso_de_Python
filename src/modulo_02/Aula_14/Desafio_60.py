# Faça um programa que leia um número qualquer e mostre o seu fatorial

# from math import factorial

# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial (n)

# print('O Fatorial do N° {}, é: {}'.format(n, f))


# OUTRA FORMA

# n = int(input('Digte um número para calcular seu fatorial: '))
# c = n
# f = 1
# print('Calculando {}! = '.format(n), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print('{}'.format(f))


# Outra forma

n = int(input("Digite um número para calcular seu fatorial: "))
f = 1
for c in range(1, n + 1):
    f *= c

print("O Fatorial de {} é {}".format(n, f))
