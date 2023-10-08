import moeda

p = float(input('Digite o Preço: R$'))
t = float(input('Digite o Valor da Taxa: '))
print(f"A Metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"O Aumento de {t}% é R${moeda.moeda(moeda.aumentar(p, t))}")
print(f"A Diminuição de {t}% é R${moeda.moeda(moeda.diminuir(p, t))}")