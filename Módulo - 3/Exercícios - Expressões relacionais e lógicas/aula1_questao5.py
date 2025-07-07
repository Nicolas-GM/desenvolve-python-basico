genero = input("Digite seu gênero (M ou F): ").strip().upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

regra_A = (genero == "F" and idade >= 60) or (genero == "M" and idade >= 65)
regra_B = tempo_servico >= 30
regra_C = idade >= 60 and tempo_servico >= 25
pode_aposentar = regra_A or regra_B or regra_C

print(f"De acordo com esses dados você pode aposentar: {pode_aposentar}")