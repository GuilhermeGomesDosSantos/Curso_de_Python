# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
divideNome = nome.split()
print('Seu primeiro nome é: {}'.format(divideNome[0]))
print('Seu último nome é: {}'.format(divideNome[len(divideNome)-1]))