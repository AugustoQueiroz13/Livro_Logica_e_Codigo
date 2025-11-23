print("--- Calculadora Imortal ---")
print("Digite 'sair' para encerrar.")

while True:
    try:
        entrada1 = input("\nNumero 1: ")
        if entrada1.lower() == 'sair': break
        n1 = float(entrada1)

        entrada2 = input("Numero 2: ")
        if entrada2.lower() == 'sair': break
        n2 = float(entrada2)

        op = input("Operacao (+, -, *, /): ")

        if op == '+': res = n1 + n2
        elif op == '-': res = n1 - n2
        elif op == '*': res = n1 * n2
        elif op == '/': res = n1 / n2
        else:
            print("Operacao desconhecida.")
            continue # Pula para o proximo loop sem erro

        print(f"Resultado: {res}")

    except ValueError:
        print("Erro: Voce digitou letras? Use apenas numeros.")
    except ZeroDivisionError:
        print("Erro: Divisao por zero e impossivel.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
