# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (Largura e Comprimento) e
# mostre a área do terreno

def area(l, c):
    area = l * c
    print(f"A área de um terreno {l} X {c} é de {area}m²")

print("Controle de Terrenos")
print("-" * 30)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)