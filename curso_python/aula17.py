condition_1 = False
condition_2 = False
condition_3 = True
condition_4 = False


def msg(condition):
    print(f'A condição atendida foi a condição {condition}')


if condition_1:
    msg(1)
elif condition_2:
    msg(2)
elif condition_3:
    msg(3)
elif condition_4:
    msg(4)
else:
    print('Nenhuma das condições foram atendidas')
