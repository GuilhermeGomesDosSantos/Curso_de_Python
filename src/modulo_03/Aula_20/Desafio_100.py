# faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint
from time import sleep
cont = 0
numeros = list()
def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.5)
    print("PRONTO!")


def somaPar(lista):
    valorPar = []
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            valorPar.append(valor)
    print(f"Somando os valores pares da {lista} temos os valores pares {valorPar}\nTemos a soma dos pares igual a {soma}")

sorteia(numeros)
somaPar(numeros)