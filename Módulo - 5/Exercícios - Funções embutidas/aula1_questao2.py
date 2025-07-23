import random
import math

n = int(input("Digite a quantidade de números aleatórios que deseja gerar: "))

soma = 0
for i in range(n):
    numero = random.randint(0, 100)
    print(numero)
    soma += numero

raiz = math.sqrt(soma)

print(f"A soma dos números é: {soma}")
print(f"A raiz quadrada da soma é: {raiz:.2f}")