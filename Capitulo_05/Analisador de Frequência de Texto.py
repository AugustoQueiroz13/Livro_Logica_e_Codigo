print("--- Analisador de Texto ---")
texto = input("Digite um paragrafo: ").lower()

# O dicionario vai guardar { 'letra' : quantidade }
frequencia = {}
6
for caractere in texto:
    # Ignora espacos e pontuacao simples (opcional)
    if caractere in " .,!?":
        continue

    # Logica de contagem
    # Se ja vi essa letra, somo 1. Se nao, comeco com 1.
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print("\nResultado:")
# Ordenando pelas chaves para ficar organizado
for letra in sorted(frequencia.keys()):
    print(f"'{letra}': {frequencia[letra]} vezes")