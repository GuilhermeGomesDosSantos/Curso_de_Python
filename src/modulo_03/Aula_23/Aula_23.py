# print(x)

# n = int(input('Número: '))
# print(f'Você digitou o Número: {n}')

# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmene tivemos um problema :(')
# else:
#     print(f'O resultador é: {r}')
# finally:
#     print('Volte sempre! Muito Obrigado!')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Problema encontrado foi {erro.__class__}')
# else:
#     print(f'O resultador é: {r}')
# finally:
#     print('Volte sempre! Muito Obrigado!')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(f'O resultador é: {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado!')