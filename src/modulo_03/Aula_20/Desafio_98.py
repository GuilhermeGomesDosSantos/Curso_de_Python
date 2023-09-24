# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens atráves da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def contador(i, f, p):

    print("-="*30)

    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        c = i
        while c <= f:
            sleep(0.5)
            print(f"{c}, ", end="", flush=True)
            c += p
        print("FIM!")

    else:
        c = i
        while c >= f:
            sleep(0.5)
            print(f"{c}, ", end="", flush=True)
            c -= p
        print("FIM!")

contador(1, 10, 1)
contador(10, 1, 2)

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
