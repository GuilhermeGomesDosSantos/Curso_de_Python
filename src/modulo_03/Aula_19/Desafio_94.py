# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas cadastradas
# B) Uma média de idade
# C) Uma lista com mulheres
# D) Uma lista com idade acima da média

pessoa = dict()
galera = []
soma = media = 0

while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F]")).strip().upper()[0]

        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F")

    pessoa["idade"] = int(input("Idade: "))

    galera.append(pessoa.copy())

    soma += pessoa["idade"]

    while True:
        res = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if res in "SN":
            break
        print("ERRO! Responda apenas S ou N")
    if res == "N":
        break
print("-=" * 30)
print(galera)

print(f"A) Total de pessoas cadastradas {len(galera)} Pessoas cadastradas")
media = soma / len(galera)

print(f"B) A média de idade é de {media:5.2f} anos")

print("C) As Mulheres cadastradas foram: ", end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f'{p["nome"]} ', end="")
print()

print("D) Lista das pessoas que estão acima da média: ")
for p in galera:
    if p["idade"] >= media:
        print("     ", end="")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
print("<< ENCERRADO >>")
