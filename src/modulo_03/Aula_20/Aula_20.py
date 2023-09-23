# def lin():
#     print('-' * 30)

# lin()
# print('     CURSO EM VÍDEO      ')
# lin()
# print('     APRENDA PYTHON      ')
# lin()
# print('     GUSTAVO GUANABARA   ')
# lin()


# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)

# titulo('    CURSO EM VÍDEO      ')
# titulo('    PYTHON E MUITO BOM! ')
# titulo('OI')

# def soma(a, b):
#     s = a + b
#     print(s)

# soma(4, 6)
# soma(7, 5)
# soma(3, 1)

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma de A + B = {s}')

# soma(4, 6)

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma entre A + B é igual ah = {s}')

# soma(b = 2, a = 9)
# soma(2, 6)

# def contador(* num):
#     print(num)

# contador(2, 1,8)
# contador(4, 9, 7, 3)
# contador(8, 0, 2)

# def contador(* num):
#     tam = len(num)
#     print(f'Recebi ps valores {num} e são ao todo {tam} números')

# contador(2, 6, 1, 5, 1)
# contador(9, 0, 8)
# contador(3, 1, 9, 3)

# def dobra(list):
#     pos = 0
#     while pos < len(list):
#         list[pos] *= 2
#         pos += 1

# valores = [5, 2, 7, 2, 8, 0]
# dobra(valores)
# print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")


soma(2, 7)
soma(1, 9, 0, 8)
