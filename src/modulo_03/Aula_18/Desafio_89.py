# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente

lista = list()

while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])

    res = " "

    while res not in "SN":
        res = str(input("Quer continuar [S/N] ? ")).strip().upper()[0]

    if res != "S":
        break

print("-=" * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-" * 26)
for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-"*35)
    opc = int(input("Mostrar notas de qual(is) aluno(s) (999m Interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(lista) - 1:
        print(f"Notas de {lista[opc][0]} são {lista[opc][1]}")

    elif opc > len(lista) - 1:
        print(f"O N° {opc} não está armazendado na Lista")
print("<<< VOLTE SEMPRE >>>")
