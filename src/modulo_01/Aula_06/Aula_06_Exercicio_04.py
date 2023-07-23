# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# e todas as informações possiveis sobre ele.

inserirValor = input('Digite um Valor: ')
print('O tipo primitivo desse valor é, ', type(inserirValor))
print('{}, é Maiusculo ? '.format(inserirValor),inserirValor.isupper())
print('{}, é Alfa Númerico ?'.format(inserirValor),inserirValor.isalnum())
print('{}, é Somente Letra ?'.format(inserirValor),inserirValor.isalpha())
print('{}, é caracter ASCII ?'.format(inserirValor),inserirValor.isascii())
print('{}, é Decimal ?'.format(inserirValor),inserirValor.isdecimal())
print('{}, é Digito ?'.format(inserirValor),inserirValor.isdigit())
print('{}, é um Identificador Valido ?'.format(inserirValor),inserirValor.isidentifier());
print('{}, é Minusculas ?'.format(inserirValor),inserirValor.islower());
print('{}, é Númerico ?'.format(inserirValor),inserirValor.isnumeric());
print('{}, é Imprimíveis ?'.format(inserirValor),inserirValor.isprintable());
print('{}, tem espaço em branco ?'.format(inserirValor),inserirValor.isspace());