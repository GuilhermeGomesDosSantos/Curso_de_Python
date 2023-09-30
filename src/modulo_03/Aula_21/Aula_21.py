# INTERACTIVE HELP
# help(print)
# print(input.__doc__)
# help(print)

# DOCSTRINGS --> é basicamente uma string de documentação

# def contador (i, f, p):
    # """
    # --> Faz uma contagem e mostra na tela
    # :param i: inicio da contagem
    # :param f: fim da contagem
    # :param p: passo da contagem
    # :return : sem retorno
    # Função criada por Guilherme Gomes
    #  """
#     c = i
#     while c <= f:
#         print(f"{c} ", end='')
#         c += 1
#     print("FIM!")
# contador(0, 10, 2)
# help(contador)

# PARÂMETROS OPCIONAIS --> vai deixar por padrão valores opcionais
# def somar(a = 0, b = 0, c = 0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     Função criado por Guilherme Gomes
#     """
#     s = a + b + c
#     print(f"A soma vale: {s}")
# somar(a = 1, c = 5)
# somar(2, 5, 8)
# somar(2, 5)
# somar(2)
# somar()

# Escopo DE VARIÁVEIS --> é um local aonde uma variavel vai e não vai existir
def funcao(n2):
    global n1
    n1 = 10
    n2 +=5
    n3 = 2
    print(f"N1 dentro vale {n1}")
    print(f"N2 dentro vale {n2}")
    print(f"N3 dentro vale {n3}")

n1 = 2
funcao(n1)
print(f"N1 global vale {n1}")

#RETORNO DE VALORES (return)
# def somar(a = 3, b = 5, c = 9):
#     s = a + b + c
#     return s

# r1 = somar(1, 5, 7)
# r2 = somar(1, 8)
# r3 = somar(1, 1)
# print(f"Os Resultados foram {r1}, {r2} e {r3}")