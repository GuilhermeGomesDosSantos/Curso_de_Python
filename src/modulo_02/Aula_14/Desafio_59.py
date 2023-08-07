# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A Multiplicação entre {} e {} é: {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é: {}'.format(n1, n2, n1))
        else:
            print('O maior nímuero entre {} e {} é: {}'.format(n1, n2, n2))
    elif opcao == 4:
        print('Insira os novos valores...')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
        print('=-='*20)
        sleep(1.5)
print('Fim do programa! Volte sempre!')