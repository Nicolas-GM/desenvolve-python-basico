n = int(input("Digite o número de respondentes: "))

soma_idades = 0
contador = 0

while contador < n:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades += idade
    contador += 1

media = soma_idades / n

print(f"Média das idades: {media:.2f}")