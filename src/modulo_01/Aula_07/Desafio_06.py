# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = int(input('Digite um Número: '))
print('O Dobro de {} vale {}'.format(num, (num * 2)))
print('O Triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(num, (num*3), num, pow(num, (1/2))))

