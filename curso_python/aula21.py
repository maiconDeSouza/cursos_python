# Operadores Lógicos
# and (e), or (ou) e not (não)
# and -> todas as condições precisam ser verdadeiras
# se qualquer valor for False, a expressão inteira será falsa
# São considerados valores Falsy:
#  -> 0, 0.0, '', None, False
var = None

print(not not var)
print(bool(var))

login_user = 'comandante'
password_user = '12345'
vazia = ''

login = input('Digite seu login: ')
password = input('Digite seu password: ')

if login == login_user and password == password_user:
    print('Usuário logado!')
else:
    print('Login ou Password inválidos')

print(f'{True=} and {True=} = {True and True}')
print(f'{True=} and {False=} = {True and False}')
print(f'{True=} and {""=} = {True and bool("")}')
print(f'{True=} and {0=} = {True and bool(0)}')
print(f'{True=} and {0.0=} = {True and bool(0.0)}')

# curto circuito
print(True and 'Dante')
print(False and 'Dona Maia')
print(True and 0 and 'Dona Maia')
print(True and 'Dona Maia' and 0)
