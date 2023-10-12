def leiaDinheiro(msg):
    validacao = False

    while not validacao:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! "{entrada}", Digite um número inteiro valido !!!\033[m')
        else:
            return float(entrada)