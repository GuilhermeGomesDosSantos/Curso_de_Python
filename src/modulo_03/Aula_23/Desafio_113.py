# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFlooat() com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO! Digite um Número Inteiro\033[m")
            continue
        except (KeyboardInterrupt):
            print(f"\033[0;31mEntrada de dados interrompida pelo Usuário!!!\033[m")
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except(ValueError, TypeError):
            print(f"\033[0;31mERRO! Digite um Número Flutuante\033[m")
            continue
        except(KeyboardInterrupt):
            print(f"\033[0;31mEntrada de dados interrompida pelo Usuário!!!\033[m")
            return 0
        else:
            return r

n = leiaInt("Digite um Número Inteiro: ")
r = leiaFloat("Digite um valor Real: ")
print(f"Você Digitou o Valor: {n}")
print(f"Você Digitou o Número: {r}")
print(f"Os valores digitados foram: N° Inteiro: {n} e N° Real: {r}")