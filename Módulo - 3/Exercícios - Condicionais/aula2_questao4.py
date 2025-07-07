distancia = float(input("Digiote a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

if distancia <= 100:
    valor_por_kg = 1.00
elif distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

frete = valor_por_kg * peso

if peso > 10:
    frete += 10.00

print(f"Valor do frete: R${frete:.2f}")