# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade)
# e um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o sala´rio.
# Calcule e acescente, além da idade, com quantos anos a pessoa vai se aposentar


from datetime import datetime

dados = dict()
dados["nome"] = str(input("Nome: "))
anoNasc = int(input("Data de Nascimento: "))
dados["idade"] = datetime.now().year - anoNasc
dados["cpts"] = int(input("Carteira de Trabalho (0 não tem): "))

if dados["cpts"] != 0:
    dados["anoContratacao"] = int(input("Ano de Contratação: "))
    dados["salario"] = float(input("Slário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados['anoContratacao'] + 35) - datetime.now().year)
print("-="*30)

for k, v in dados.items():
    print(f" - {k} tem o valor {v}")
