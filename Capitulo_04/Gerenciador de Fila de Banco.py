fila = []

print("--- Sistema de Fila do Banco ---")
while True:
    print(f"\nFila atual: {fila}")
    print("1. Chegou cliente")
    print("2. Atender proximo")
    print("3. Sair")

    op = input("Opcao: ")

    if op == "1":
        nome = input("Nome do cliente: ")
        fila.append(nome)
    elif op == "2":
        if len(fila) > 0:
            atendido = fila.pop(0) # Remove do indice 0
            print(f"Chamando cliente: {atendido}")
        else:
            print("A fila esta vazia!")
    elif op == "3":
        break
    else:
        print("Opcao invalida.")