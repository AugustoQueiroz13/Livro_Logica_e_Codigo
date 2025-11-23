print("=== TABUADA COMPLETA (1 a 10) ===\n")

# loop externo: Controla o numero da tabuada
for numero_da_tabuada in range(1, 11):
    print(f"--- Tabuada do {numero_da_tabuada} ---")
    
    # loop interno multiplica de 1 ao 10
    for multiplicador in range(1, 11):
        resultado = numero_da_tabuada * multiplicador
        # Formatação f-string para exibir bonitinho: 5 x 1 = 5
        print(f"{numero_da_tabuada} x {multiplicador} = {resultado}")
    
    print("") # Pula uma linha entre uma tabuada e outra para organizar

print("Fim das tabuadas!")