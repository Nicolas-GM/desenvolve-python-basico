idade = int(input("Digite a sua idade: "))
ja_jogou_3_ou_mais = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True ou False): ").lower()
ja_jogou_3_ou_mais = ja_jogou_3_ou_mais == "true"
vitorias = int(input("Quantas vezes você venceu um jogo de tabuleiro? "))

pode_entrar = (16 <= idade <=18) and ja_jogou_3_ou_mais and (vitorias >= 1)
print(f"Apto para ingressar no clube de jogos de tabuleiro: {pode_entrar}")