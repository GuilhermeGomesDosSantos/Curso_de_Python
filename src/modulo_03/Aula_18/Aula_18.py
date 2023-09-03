# teste = list()
# teste.append("Gui")
# teste.append("20")
# galera = list()
# galera.append(teste[:])
# teste[0] = "Maria"
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [["João", 19], ["Ana", 33], ["Joaquin", 13], ["Maria", 45]]
# print(galera)
# print(galera[0])
# print(galera[0][0])
# print(galera[2][1])

# for p in galera:
#     print(p)

# for p in galera:
#     print(p[0])

# for p in galera:
#     print(p[1])

# for p in galera:
    # print(f"{p[0]} tem {p[1]} anos de idade")

# galera = list()
# dado = list()

# for c in range(0, 5):
#     dado.append(str(input("Nome: ")))
#     dado.append(int(input("Idade: ")))
#     galera.append(dado[:])
#     dado.clear()
# print(galera)

# galera = list()
# dado = list()

# for c in range(0, 5):
#     dado.append(str(input("Nome: ")))
#     dado.append(int(input("Idade: ")))
#     galera.append(dado)
#     dado.clear()
# print(galera)

galera = list()
dado = list()
totmai = 0
totmen = 0

for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1

print(f"Temos {totmai} maiores e {totmen} menores de idade")