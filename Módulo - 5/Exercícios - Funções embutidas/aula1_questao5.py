import emoji

emojis = {
    ":red_heart:" : ":red_heart:",
    ":thumbs_up:" : ":thumbs_up:",
    ":thinking_face:" : ":thinking_face:",
    ":partying_face:" : ":partying_face:"
}

print("Emojis disponíveis:\n")

for codigo, descricao in emojis.items():
    emoji_visual = emoji.emojize(codigo, language='alias')
    print(f"{emoji_visual}  - {codigo}")

frase = input("\nDigite uma frase usando os códigos de emoji acima e ela será emojizada:\n")
frase_emojizada = emoji.emojize(frase, language='alias')

print("Frase emojizada:")
print(frase_emojizada)