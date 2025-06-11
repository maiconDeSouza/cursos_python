a = 'A'
b = 'B'
c = 1.1

result = '{}-{}-{}'.format(a, b, c)
print(result)

# formatação
print('{} -- {} -- {:.2f}'.format(a, b, c))
# Pelo indice
print('{2:.2f} -- {1} -- {0}'.format(a, b, c))
# Parametro nomeado
print('{nomeado_2} -- {nomeado_3:.2f} -- {nomeado_1}'.format(nomeado_1=a,
      nomeado_2=b, nomeado_3=c))
