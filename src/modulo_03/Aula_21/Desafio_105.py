# Faça um programa que tenha uma função notas() que receber várias notas de alunos
# e vai retornar um dicioncionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings

def notas(*n, situacao = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    : parametro n: Uma ou mais Notas do alunos (Aceita várias)
    : parametro situacao: Valor Opcional, indicando se deve ou não adicionar a situação
    : return: Dicionário com vários informações sobre a situação da turma.
    """
    dicionario = dict()

    dicionario["quantidade"] = len(n)
    dicionario["maior"] = max(n)
    dicionario["menor"] = min(n)
    dicionario["media"] = sum(n)/len(n)

    if situacao == True:
        if dicionario["media"] >= 7:
            dicionario["situacao"] = "BOA!"
        elif dicionario["media"] >= 5:
            dicionario["situacao"] = "RAZOAVEL!"
        else:
            dicionario["situacao"] = "RUIM!"

    return dicionario

resp = notas(8, 5, 10, 1, situacao=True)
print(resp)
help(notas)