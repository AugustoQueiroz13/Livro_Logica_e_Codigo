print("--- Controle de Acesso ---")
idade = int(input("Idade: "))
tem_convite = True # Simulacao

if idade >= 60:
    print("VIP: Entrada Gratuita.")
elif idade >= 18 and tem_convite:
    print("Entrada Liberada.")
elif idade >= 18 and not tem_convite:
    print("Barrado: Precisa de convite.")
else:
    print("Barrado: Menor de idade.")
