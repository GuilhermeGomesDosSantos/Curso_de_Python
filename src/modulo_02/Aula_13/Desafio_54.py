# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

anoAtual = date.today().year
maiordeIdade = 0
menordeIdade = 0

for c in range(1, 8):
    anoPessoa = int(input("Em que anoa a {}° pessoa nasceu? ".format(c)))
    idade = anoAtual - anoPessoa 
    if idade >= 18:
        maiordeIdade += 1
    else:
        menordeIdade += 1

print("Ao todo tivemos {} pessoas maiores de Idade".format(maiordeIdade))
print("E também tivemos {} pessoas menores de idades".format(menordeIdade))
