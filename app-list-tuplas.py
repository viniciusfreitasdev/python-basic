# Notes - Implementação de tupla e lista
lista = ['Weg', 'Raia Drograsil', 'Vale', 'Lojas Renner']
lista = list(['Weg', 'Raia Drograsil', 'Vale', 'Lojas Renner'])

print(lista)

# Notes - Tipos diferentes
lista_vazia = []
lista_type = ['flamengo', 8, 'campeonatos brasileiros']

# Notes - Matriz 3x3
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in matriz:
  for item in lista:
    print(item, end=' ')
  print()
  
# Notes - Adicionando Item a lista
lista_vazia.append('Compra tudo')
lista_vazia.append('Vende um pouco')
lista_vazia.append('Vende sua casa para comprar')
lista_vazia.append('Compra devagar')
lista_vazia.append('Vende rápido ou vai quebrar')
lista_vazia.append('Compra mais')

print(f"Lista:{lista_vazia}")

# Notes - Selecionando Elementos na lista
print(f"Posição 0: {lista_vazia[0]}")
print(f"Posição 1: {lista_vazia[1]}")
print(f"Posição -1: {lista_vazia[-1]}")

# Notes - Selecionando Elementos na Matriz
print(f"Matriz [0]: {matriz[0]}")
print(f"Matriz [0][0]: {matriz[0][0]}")

# Notes - Selecionando vários elementos
print(f"Lista [0:2]: {lista_vazia[0:2]}") # Busca de indicie ate outro
print(f"Lista [1:]: {lista_vazia[1:]}")   # Busca a partir dessa indice
print(f"Lista [:3]: {lista_vazia[:3]}")   # Busca ate esse indice
print(f"Lista [-2:]: {lista_vazia[-2:]}") # Busca ate esse indice ( de trás para frente )

# Notes - Alterando elementos
lista_vazia[0] = 'vende'
print(f"Posição 0: {lista_vazia[0]}")

# Notes - Inserindo em uma posição
lista_vazia.insert(2, 'Compra até acabar o caixa')
print(f"Lista: {lista_vazia}")

# Notes - Removendo elementos da lista
lista_vazia.remove('Compra até acabar o caixa')
print(f"Lista: {lista_vazia}")

# Notes - Removendo usando uma posição especifica
del lista_vazia[0]
print(f"Lista: {lista_vazia}")

# Notes - Verificando se elemento está na lista
verificando = "compra tudo" in lista_vazia
verificando2 = "compra tudo" not in lista_vazia

print(verificando, verificando2)

# Notes - Junção de lista
lista01 = [1, 2, 3]
lista02 = [4, 5, 6]
lista03 = lista01 + lista02
print(f"Lista Juntada: {lista03}")


# Notes - Ordenação de lista
desordenada = [56, 45, 1, 75, 23]
cresente = sorted(desordenada)
decresente = sorted(desordenada, reverse=True)

print(f"Lista desordenada: {desordenada}")
print(f"Lista ordenada de forma cresente: {cresente}")
print(f"Lista ordenada de forma descresente: {decresente}")

# Notes - Extraindo Tamanho, Maximos, Minimos e Media de uma lista
print(len(desordenada)) # Retorna tamanho
print(max(desordenada)) # Retorna valor maximo
print(min(desordenada)) # Retorna valor minimo
print(sum(desordenada)/len(desordenada)) # Retorna valor médio

print('*' * 40)
tupla = (2, 3, 5, 2, 2)

print(tupla.count(2)) # Quantas vezes o objeto aparece na tupla
print(tupla.index(2)) # Retorno baseano no indice

print(len(desordenada))
print(len(tupla))

print('*' * 20, ' Exercicios ', '*' * 20)

# Exercicio 11
empresas = ('1 - Empresa01', '2 - Empresa02', '3 - Empresa03', '4 - Empresa04')
recomendacao = ('Não compra', 'Compra', 'Compra Tudo', 'Vende')

print('Lista de empresas')
for i in empresas:
  print(i)
  
escolha = int(input('Escolha uma empresa para exibir a recomendação de compra:'))

print(f"A recomendação de compra da empresa {empresas[escolha-1]} é: {recomendacao[escolha-1]}")

# Exercicio 12
empresaNome = ('1 - Empresa01', '2 - Empresa02', '3 - Empresa03', '4 - Empresa04', '5 - Empresa05')
empresaPreco2 = [10, 20, 30, 40, 50, 10]
empresaLucro2 = [11, 22, 5, 50, 100]

empresaPreco = []
empresaLucro = []

print('Digite o Preço e Lucro das seguintes empresas')

for i in empresaPreco2:
  empresaPreco.append(i)

for i in empresaLucro2:
  empresaLucro.append(i)

# for i in empresaNome:
#   print(f"Empresa: {i}")
#   tempPreco = input(f"Qual o preço da empresa {i}: ")
#   tempLucro = input(f"Qual o lucro da empresa {i}: ")
#   empresaPreco.append(tempPreco)
#   empresaLucro.append(tempLucro)

indicePrecoMin = empresaPreco.index(min(empresaPreco))
indiceLucroMin = empresaLucro.index(min(empresaLucro))

indicePrecoMax = empresaPreco.index(max(empresaPreco))
indiceLucroMax = empresaLucro.index(max(empresaLucro))

print(f"A empresa com MENOR PREÇO foi a {empresaNome[indicePrecoMin]} com valor de {empresaPreco[indicePrecoMin]}")
print(f"A empresa com MENOR LUCRO foi a {empresaNome[indiceLucroMin]} com valor de {empresaLucro[indiceLucroMin]}")

print(f"A empresa com MAIOR PREÇO foi a {empresaNome[indicePrecoMax]} com valor de {empresaPreco[indicePrecoMax]}")
print(f"A empresa com MAIOR LUCRO foi a {empresaNome[indiceLucroMax]} com valor de {empresaLucro[indiceLucroMax]}")

print(empresaNome)
print(empresaPreco)
print(empresaLucro)


