# print('\033[31mOlá, Mundo!')
# print('\033[31;43mOlá, Mundo!')
# print('\033[1;31;43mOlá, Mundo\033[m!')
# print('\033[4;30;45mOlá, Mundo\033[m!')
# print('\033[7;30mOlá, Mundo\033[m!')
# print('\033[0;33;44mOlá, Mundo\033[m!')

a = 3
b = 5
# print('Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m!!!'.format(a, b))

nome = 'Guilherme'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m]'}
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
# print('Olá! Muito prazer em te conhecer, {}{}!!!'.format('\033[4;34m', nome))
print('Olá! Muito prazer em te conhecer, {}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))