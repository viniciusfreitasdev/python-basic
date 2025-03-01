# Notes - Sets
set_teste = {'weg', 'renner', 'c&a', 'SLC Agricola'}
set_numero = {1, 4, 5, 8}

print(set_teste)

# Notes - Remover duplicadas
lista_duplicada = ['renner', 'renner', 'weg', 'weg']
lista_unica = list(set(lista_duplicada)) # Pode converter listas em sets ou tuplas sem problemas
print(lista_unica)

# Notes - Adicionando elementos a sets
set_numero.add(10) # Adicionando somente 1 elemento
print(set_numero)

set_numero.update([20, 25, 60]) # Adicinando +1 elemento
print(set_numero)

set_numero.discard(1) # Removendo elemento do set
print(set_numero)

set_base = {1, 2, 3, 5, 8, 9}
set_base_2 = {1, 4, 5, 6, 8, 11, 12}

print("***** União *****")
print(f"Set Concatenado: {set_base | set_base_2}")
print(f"Set Union: {set_base.union(set_base_2)}")

print("Interseção - Tem que estar nos dois ao mesmo tempo")
print(f"Interseção '&': {set_base & set_base_2}")
print(f"Interseção Intersection: {set_base.intersection(set_base_2)}")

print("Diferença = Só pode estar presente no set 1")
print(f"Diferença '-': {set_base & set_base_2}")
print(f"Diferença difference: {set_base.difference(set_base_2)}")

# Exercicio 

nome = input('Digite seu nome: ')

print(f"Olá {nome}, como você está?")
print("Estamos coletando informações de duas carteiras de investimento diferentes")
print("Poderia nos ajudar fornecendo o nome de 3 empresas?")

empresa00 = input('Digite o nome de uma empresa:')
empresa01 = input('Digite o nome de uma empresa:')
empresa02 = input('Digite o nome de uma empresa:')

print('Obrigado pelas informações! Poderia nos fornecer dados de mais 3 empresas?')
empresa10 = input('Digite o nome de uma empresa:')
empresa11 = input('Digite o nome de uma empresa:')
empresa12 = input('Digite o nome de uma empresa:')

print('Ótimo, agora nós podemos fornecer as informações necessárias')

set_empresas = {empresa00, empresa01, empresa02}
set_empresas2 = {empresa10, empresa11, empresa12}

set_difference = set_empresas.difference(set_empresas2)
set_intersection = set_empresas.intersection(set_empresas2)
set_union = set_empresas.union(set_empresas2)

print(f"A diferença entre a carteira 1 e 2 são as ações {set_difference}")
print(f"A interseção entre a carteira 1 e 2 são as ações {set_intersection}")
print(f"A união entre a carteira 1 e 2 são as ações {set_union}")