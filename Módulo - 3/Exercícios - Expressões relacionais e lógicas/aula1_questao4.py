classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de Força (de 1 a 20): "))
magia = int(input("Digite os pontos de Magia (de 1 a 20): "))

if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = 5 < forca <= 15 and 5 < magia <= 15
else:
    valido = False

print(f"Pontos de atributo consistentes com a classe escolhida: {valido}")