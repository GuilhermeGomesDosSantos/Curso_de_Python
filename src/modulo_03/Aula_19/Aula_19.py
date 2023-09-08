pessoas = {"nome": "Gui", "sexo": "M", "idade": 20}
# print(pessoas)
# print(pessoas[0]) #Vai dar erro
# print(pessoas['nome'])
# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(f"{k}")

# del pessoas["sexo"]

# for k, v in pessoas.items():
#     print(f"{k} = {v}")

# pessoas["nome"] = 'Guilherme'
# pessoas["peso"] = 96.5

# for k, v in pessoas.items():
#     print(f"{k} = {v}")

# brasil = list()
# estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# estado2 = {"uf": "São Paulo", "sigla": "SP"}
# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['sigla'])
# print(brasil[1]['sigla'])

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input("Unidade Federativa: "))
#     estado['sigla'] = str(input("Sigla do Estado: "))
#     brasil.append(estado.copy())
# print(brasil)

estado = dict()
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())

# for e in brasil:
#     for k, v in e.items():
#         print(f"O campo {k} tem valor {v}.")

# for e in brasil:
#     for v in e.values():
#         print(v)

for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()