# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos

maior18 = 0
totalHomens = 0
mulherMenos20 = 0
cont = 0


while True:
    print("-" * 30)
    print("CADASTRO DE PESSOA")
    print("-" * 30)

    idade = int(input("Idade: "))

    if idade >= 18:
        maior18 += 1

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

    if sexo == "M":
        totalHomens += 1

    if sexo == "F" and idade < 20:
        mulherMenos20 += 1

    res = " "
    while res not in "SN":
        print("-" * 30)
        res = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if res != "S":
        break
print(f"Total de Pessoas com mais de 18 anos: {maior18}")
print(f'Ao todo temos {totalHomens} Homen(s) cadastrados')
print(f'E temos {mulherMenos20} mulhere(s) com menos de 20 anos')
