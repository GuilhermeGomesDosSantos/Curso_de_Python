# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep


def maior(*num):
    numMaior = 0
    cont = 0

    print("\nAnalisando os valores passados...")
    for valor in num:
        print(f"{valor} ", end="", flush=True)
        sleep(0.5)

        if valor > numMaior:
            numMaior = valor
        else:
            if cont == 0:
                numMaior = valor
        cont += 1

    print(f"Foram informados {cont} valores ao todo")
    print(f"O maior Número é {numMaior}")


maior(2, 4, 6, 1, 4, 2)
maior(5, -1, 3, -2, 10)
maior(20, 3, 1)
maior(4, 2, 1)
maior(0, -1, -4, -6)
maior()