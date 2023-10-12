# Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.

def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    res =  preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco, formato = False):
    res = preco / 2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco, taxaAumento = 10, taxaReducao = 10):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'Com {taxaAumento:.2f}% de Aumento: \t{aumentar(preco, taxaAumento, True)}')
    print(f'Com {taxaReducao:.2f}% de Redução: \t{diminuir(preco, taxaReducao, True)}')
    print('-' * 30)