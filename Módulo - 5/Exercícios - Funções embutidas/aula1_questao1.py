numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

diferenca = abs(numero1 - numero2)
diferenca_arredondada = round(diferenca, 2)

print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")