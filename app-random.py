import random
from random import choice

# Notes - 0 and 1
# print(f"{random.random():.2f}")

#Notes - 10 and 100
# print(f"{random.uniform(10, 100):.2f}")

#Notes - 10 and 100 ( Integer)
# print(f"{random.randint(10, 100)}")

#Notes - Distribuição normal
# print(f"{random.gauss(10, 30):.2f}")

# Notes - Teste de sorteio
tickers = ['WEGE3', 'PCAR3', 'LREN3']
escolhida = random.choice(tickers)
print(f"Empresa escolhida é: {escolhida}")

# Exercio 9
moeda = ['Cara', 'Coroa']
print(f"Resultado de tirar na moeda: {random.choice(moeda)}")
print(f"Resultado de tirar na moeda: {choice(['cara', 'coroa'])}")

# Exercicio 10
print(f"A nota da sua prova foi {random.randint(0, 10)}")