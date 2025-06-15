# if / elif / else
enter_or_leave = input('Vocẽ quer "entrar" ou "sair"? ')

if enter_or_leave == 'entrar':
    print('Você acabou de entrar no sistema')
elif enter_or_leave == 'sair':
    print('Você acabou de sair do sistema')
else:
    print('Texto invalido!')
    print('Digite apenas "entrar" ou "sair"')
