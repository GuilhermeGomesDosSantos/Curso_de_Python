# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter
ranking = list()

jogo = {
    "Jogador_1": randint(0, 6),
    "Jogador_2": randint(0, 6),
    "Jogador_3": randint(0, 6),
    "Jogador_4": randint(0, 6),
}

print("Valores Sorteados.")

for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)

print("-="*30)
print(" == RANKING DOS JOGADORES == ")

for i, v in enumerate(ranking):
    print(f'{i+ 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)