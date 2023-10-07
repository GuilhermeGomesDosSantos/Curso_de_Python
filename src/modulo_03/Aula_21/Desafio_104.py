# Crie um programa que tenha a função leiaint(), que vai funcionar de forma
# semelhantw à função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico

# Ex: n = leiaInt('Digite um n')

# def leiaInput(msg):
#     ok = False
#     valor = 0

#     while True:
#         n = str(input(msg))

#         if n.isnumeric():
#             valor = int(n)
#             break
#         else:
#             print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m\nO valor Digitado '{n}' não é do Tipo Númerico")
#             break
#     return valor

# n = leiaInput("Digite um Número: ")
# print(f"Você Digitou o Valor {n}")

# OU

def leiaInput(msg):
    ok = False
    valor = 0

    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"\033[0;31mERRO! Digite um Número Inteiro\033[m")

        if ok == True:
            break
    return valor

n = leiaInput("Digite um Número: ")
print(f"Você Digitou o Valor: {n}")