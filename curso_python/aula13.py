name = 'Luiz Otávio'
height = 1.80
weight = 95
imc = weight / (height * height)

result = f'{name} tem {height:.2f} de altura e pesa {weight}kg e seu imc é de {imc:.2f}'

print(result)

print(...)

# Usando para reais por exemplo:
price = 87.35
discount = 15
total = price - (price * (discount / 100))
result_discount = f'O produto com desconto sai R${total:,.2f}'
print(result_discount)
