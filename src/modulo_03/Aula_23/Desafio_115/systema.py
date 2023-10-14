# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples.

# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas



from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):

    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o coneúdo de um arquivo!
        lerArquivo(arq)


    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')

        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarArq(arq, nome, idade)


    elif resposta == 3:
        # Opção de sair do sistema
        cabecalho('Saindo do Sistema... Até Logo !')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.2)