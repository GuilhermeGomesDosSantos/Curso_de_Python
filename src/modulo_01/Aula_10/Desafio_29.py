# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem
# Dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite

velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(
        "MULTA! Você excedeu o limite permitido que é de 80Km/h\n"
        + "Você deve pagar uma multa de R${}!".format(multa)
    )
print("Tenha um Bom dia! Dirija com segurança")
