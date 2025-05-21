nome_1       = input("Digite o nome do produto 1: ")
valor_1      = float(input("Digite o valor unitário do produto 1: "))
quantidade_1 = int(input("Digite a quantidade do produto 1: "))
nome_2       = input("\nDigite o nome do produto 2: ")
valor_2      = float(input("Digite o valor unitário do produto 2: "))
quantidade_2 = int(input("Digite a quantidade do produto 2: "))
nome_3       = input("\nDigite o nome do produto 3: ")
valor_3      = float(input("Digite o valor unitário do produto 3: "))
quantidade_3 = int(input("Digite a quantidade do produto 3: "))

tota_1 = valor_1 * quantidade_1
tota_2 = valor_2 * quantidade_2
tota_3 = valor_3 * quantidade_3

print(f"\nTotal: R${tota_1 + tota_2 + tota_3:,.2f}\n")