# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos -> tipos primitivos geralmente são tipos que conseguimos
# escrever de forma literal no código
# str, int, float e bool


# print('1' + 1) ao contrario do javaScript que faria a conversão de tipos neste caso
# por isso é uma linguagem de programação dinamica e fracamente tipada
# Já o python é uma linguagem dinamica e fortemente tipada, pois o intepretador não vai fazer conversões
# sem que não seja informado no código

print(int('1') + 1)
# Aqui chamamos a classe construtora de int para fazer a conversão de tipos

traco = 5 * '----'
print(traco, 'conversão de bool', traco)
print(f'string vazia -> "" = {bool("")}')
print(f'string com espaço -> " " = {bool(" ")}')
