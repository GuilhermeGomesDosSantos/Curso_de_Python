from utilidadescev import moeda, dado

p = dado.leiaDinheiro('Digite o Preço: R$')
t = dado.leiaDinheiro('Digite o Valor da Taxa: ')
r = dado.leiaDinheiro('Digite o Valor da Redução: ')
moeda.resumo(p, t, r)