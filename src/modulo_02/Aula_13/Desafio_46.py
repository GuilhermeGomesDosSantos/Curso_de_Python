# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep
print('CONTAGEM REGRESSIVA...')

for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)

print('BUM! BUM! POOW!')