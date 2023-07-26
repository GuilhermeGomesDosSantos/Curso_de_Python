# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# apresentação de trabalhos dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada

# import random
from random import shuffle
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
# random.shuffle(lista)
shuffle(lista)
print('A ordem da apresentação será: ')
print(lista)