# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro do Futebol
# na ordem de colocação. Depois
# A) Os 5 primeiros
# B) Os últimos 4 colocados
# C) Times em ordem alfabética
# D) Em que posição está o time da Chapecoense

times = ('Santos', 'Palmeiras', 'Corinthias', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Pauloa', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*15)
# print(f'Lista de times do Brasileirão: {times}')
# print('-='*15)
# print(f'Os 5 Primeiros são: {times[:4]}')
print('-='*15)
print(f'Os ultimos 4 são: {times[-4:]}')
print('-='*15)
print(f'Times em Ordem Alfabética: {sorted(times)}')
print('-='*15)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}° Posição')