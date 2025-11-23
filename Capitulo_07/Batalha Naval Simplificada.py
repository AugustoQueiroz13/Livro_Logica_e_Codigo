import random

def criar_tabuleiro():
    # Cria matriz 5x5 com 'agua' (~)
    return [["~"] * 5 for _ in range(5)]

def imprimir_tabuleiro(tab):
    print(" 0 1 2 3 4")
    for i, linha in enumerate(tab):
        print(f"{i} " + " ".join(linha))

def jogar():
    tabuleiro = criar_tabuleiro()
    # Esconde o navio
    navio_lin = random.randint(0, 4)
    navio_col = random.randint(0, 4)

    tentativas = 0
    max_tentativas = 5

    print("--- BATALHA NAVAL ---")

    while tentativas < max_tentativas:
        imprimir_tabuleiro(tabuleiro)
        print(f"\nTentativa {tentativas+1} de {max_tentativas}")

        try:
            l = int(input("Linha (0-4): "))
            c = int(input("Coluna (0-4): "))

            if l == navio_lin and c == navio_col:
                print("\nPARABENS! Voce afundou o navio!")
                tabuleiro[l][c] = "X"
                imprimir_tabuleiro(tabuleiro)
                break
            else:
                if tabuleiro[l][c] == "~":
                    print("\nAgua! Tente de novo.")
                    tabuleiro[l][c] = "O" # Marca o erro
                else:
                    print("\nVoce ja atirou ai!")

        except (ValueError, IndexError):
            print("Coordenada invalida!")

        tentativas += 1
    else:
        print(f"\nGame Over! O navio estava em {navio_lin}, {navio_col}")

jogar()