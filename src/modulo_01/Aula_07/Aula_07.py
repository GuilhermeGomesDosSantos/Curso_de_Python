# ORDEM DE PRECEDÊNCIA
# 1° ()
# 2°**
# 3°* / // %
# 4° + -

nome = input('Qual é o Seu Nome? ')
# print('Prazer em te conhecer {}!'.format(nome))
# print('Prazer em te conhecer {:20}!'.format(nome))
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'.format(nome))
# print('Prazer em te conhecer {:^20}!'.format(nome))
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# print('A soma é {}, \no produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
# print('A Divisão inteira {} e potência {}'.format(di, e))
print ('A soma é {}, A Multiplicação é {}, A divisão é {:.3f}'.format(s, m, d), end='>>>')
print ('A Divisão inteira é {}, e a Potência é {}'.format(di, e))