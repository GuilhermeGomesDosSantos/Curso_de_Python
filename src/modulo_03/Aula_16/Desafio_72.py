# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte.
# Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostrá-la por extenso

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
tupla = ''

while True:
    num = int(input('Digite um Numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o Numero: {cont[num]}')