valor = int(input("Informe o valor a ser recebido: "))

notas_de_100 = valor // 100
valor = valor % 100
notas_de_50 = valor // 50
valor = valor % 50
notas_de_20 = valor // 20
valor = valor % 20
notas_de_10 = valor // 10
valor = valor % 10
notas_de_5 = valor // 5
valor = valor % 5
notas_de_2 = valor // 2
valor = valor % 2
notas_de_1 = valor

print("\nVocê receberá a seguinte quantidade de notas:\n")
print(f"{notas_de_100} nota(s) de 100.")
print(f"{notas_de_50} nota(s) de 50.")
print(f"{notas_de_20} nota(s) de 20.")
print(f"{notas_de_10} nota(s) de 10.")
print(f"{notas_de_5} nota(s) de 5.")
print(f"{notas_de_2} nota(s) de 2.")
print(f"{notas_de_1} nota(s) de 1.\n")