import moeda

p = float(input('Digite o Preço: R$'))
t = float(input('Digite o Valor da Taxa: '))
print(f"A Metade de R${p} é R${moeda.metade(p)}")
print(f"O Dobro de R${p} é R${moeda.dobro(p)}")
print(f"O Aumento de {t}% é R${moeda.aumentar(p, t)}")
print(f"A Diminuição de {t}% é R${moeda.diminuir(p, t)}")