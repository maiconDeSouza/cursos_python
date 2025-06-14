name = input('Qual é seu nome? ')
print(f'Olá {name}, tudo bem?')
# forma para pegar o nome da variável juntamente com seu valor
print(f'{name=}')

# Não é uma boa pratica já converter para um Int() assim que recebemos o valor
number_1 = int(input(f'{name} digite um número: '))
number_2 = int(input(f'{name} digite outro número: '))


print(f'A soma de {number_1} + {number_2} = {number_1 + number_2}')


# number_1 = input(f'{name} digite um número: ')
# number_2 = input(f'{name} digite outro número: ')

# try:
#     int_number_1 = int(number_1)
#     int_number_2 = int(number_2)
#     print(
#         f'A soma de {number_1} + {number_2} = {number_1 + number_2}')
# except Exception as e:
#     print('Digite apenas numeros inteiros', e)
