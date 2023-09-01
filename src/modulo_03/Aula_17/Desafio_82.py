

# crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados,
# reséctivamente. Ao final, mostre o conteúdo das três listas geradas


valores = list()
listaPar = list()
listaImpar = list()

while True:
    valores.append(int(input("Digite um número: ")))

    res = " "

    while res not in "SN":
        res = str(input("Quer continuar ? [S/N] ")).strip().upper()[0]

    if res != "S":
        break

for i, v in enumerate(valores):
    if v % 2 == 0:
        listaPar.append(v)
        
    elif v % 2 == 1:
        listaImpar.append(v)

print("-=" *30)
print(f"A lista completa é {valores}")
print(f"A lista de pares é {listaPar}")
print(f"A lista de ímpares é {listaImpar}")
