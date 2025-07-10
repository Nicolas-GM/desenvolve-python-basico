n = int(input("Digite o número de experimentos: "))

total = 0
sapos = 0
ratos = 0
coelhos = 0

i = 0

while i < n:
    entrada = input(f"Experimento {i + 1} (formato: quantidade tipo): ").split()
    quantidade = int(entrada[0])
    tipo = entrada[1].upper()

    total += quantidade

    if tipo == 'C':
        coelhos += quantidade
    elif tipo == 'R':
        ratos += quantidade
    elif tipo == 'S':
        sapos += quantidade
    
    i += 1

percentual_coelhos = (coelhos / total) * 100
percentual_ratos = (ratos / total) * 100
percentual_sapos = (sapos / total) * 100

print("\nRELATÓRIO FINAL:")
print(f"Total de cobaias: {total}")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")