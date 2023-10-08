import moeda

p = float(input('Digite o Preço: R$'))
t = float(input('Digite o Valor da Taxa: '))
print(f"A Metade de R${moeda.moeda(p)} é R${(moeda.metade(p, True))}")
print(f"O Dobro de R${moeda.moeda(p)} é R${(moeda.dobro(p, True))}")
print(f"O Aumento de {t}% é R${(moeda.aumentar(p, t, True))}")
print(f"A Diminuição de {t}% é R${(moeda.diminuir(p, t, True))}")