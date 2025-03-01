# numero01 = int(input('Digite um numero:'))
# numero02 = int(input('Digite outro numero:'))

# if numero01 == 0 or numero02 == 0:
#   div = div_int = div_res = 'Não existe divisão por zero(0)'
# else:
#   div = numero01 / numero02
#   div_int = numero01 // numero02
#   div_res = numero01 % numero02

# print(f'Soma:{ numero01 + numero02 }')
# print(f'Subtração:{ numero01 - numero02 }')
# print(f'Multiplicação:{ numero01 * numero02 }')
# print(f'Divisão:{ div }')
# print(f'Potencia:{ numero01 ** numero02 }')
# print(f'Divisão Inteira:{ div_int }')
# print(f'Resto de uma divisão :{ div_res }')
# print('*' * 40)

# Notes - Exercicio 7
empresa = input('Digite o ticker da empresa: ')
cotacao = float(input('Digita a cotação aqui: '))
print(f"Caso a empresa {empresa} suba 100%, a cota será {cotacao * 2}")
print(f"Caso a empresa {empresa} caia 50%, a cota será {cotacao / 2}")

# Notes - Exercicio 8
numero = float(input('Digite um numero:'))
print(f"O dobro do {numero} é {numero * 2}")
print(f"A raiz quadrada do {numero} é {numero ** 0.5:.2f}")

print(f"A divisão por 2 do {numero} é {numero / 2}")
print(f"Antecessor do {numero} é {numero - 1}")
print(f"Sucessor do {numero} é {numero + 1}")