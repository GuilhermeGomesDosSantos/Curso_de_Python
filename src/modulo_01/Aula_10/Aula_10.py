# nome = str(input('Qual é o seu nome? '))
# if nome == 'Guilherme':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

#===================================================

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# media = (n1 + n2) / 2
# print('A sua média foi {:.1f}'.format(media))
# if (media >= 6):
#     print('Sua média foi boa! PARABENS')
# else:
#     print('Sua média foi ruim! ESTUDE MAIS!')

#===================================================

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(media))
print('PARABENS' if media >= 6 else 'ESTUDE MAIS')