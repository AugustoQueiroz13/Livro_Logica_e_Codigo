numero_secreto = 42
tentativas = 0

print("Adivinhe o numero secreto!")

while True:
    chute = int(input("Seu chute: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"Parabens! Voce acertou em {tentativas} tentativas.")
        break
    elif chute > numero_secreto:
         print("Menos...")
    else:
        print("Mais...")