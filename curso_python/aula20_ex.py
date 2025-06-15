value_1 = input('Digite o primeiro valor: ')
value_2 = input('Digite o segundo valor: ')

int_value_1 = int(value_1)
int_value_2 = int(value_2)

if int_value_1 > int_value_2:
    print(f'O {value_1=} é maior que o {value_2=}')
elif int_value_1 < int_value_2:
    print(f'O {value_2=} é maior que o {value_1=}')
elif int_value_1 == int_value_2:
    print(f'O {value_1=} é igual {value_2=}')
