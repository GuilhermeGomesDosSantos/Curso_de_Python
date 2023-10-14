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
        cabecalho('Opção 1')

        lerArquivo(arq)
        
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo !')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.2)