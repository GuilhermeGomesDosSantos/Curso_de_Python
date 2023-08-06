# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
# desconsiderando os espaços
# APOS A SOPA
# A SACADA DA CASA


# frase = str(input('Digite uma frase: ')).strip().upper()

# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range (len(junto) -1, -1, -1):
#     inverso += junto[letra]
# print(junto, inverso)

# if inverso == junto:
#     print('Temos um Palíndromo')
# else:
#     print('Não é palíndromo')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um palíndromo!')