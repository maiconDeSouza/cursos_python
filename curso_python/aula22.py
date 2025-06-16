# Para o or é necessário que apenas uma condição seja verdadeira

enter_or_leave = input('Digite E[ntrar] ou S[air]: ')

if enter_or_leave == 'E' or enter_or_leave == 'e':
    print('Você entrou no sistema')
elif enter_or_leave == 'S' or enter_or_leave == 's':
    print('Você saiu do sistema')
else:
    print('Valor digitado inválido!')

# curto circuito
print(False or False or True or False)
print(0 or 'Casa')
print(bool(0) or 'Casa')

# Ele para a primeira verdadeira
a_real = False or False or 'Dante' or False
print(a_real)

a_real_or = 0 or 'Dante' or 'Dona Maia' or False
a_real_end = 0 and 'Dante' and 'Dona Maia' and False
print(f'{a_real_or=}')
print(f'{a_real_end=}')

print()
print(15 * '-', 'Curto circuito com senha', 15 * '-')
password = input('Digite sua senha: ') or 'Sem senha!'
print(password)
