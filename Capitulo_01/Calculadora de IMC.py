# 1. Entrada de Dados
# Convertemos para float imediatamente pois peso e altura podem ser decimais
print("--- Calculadora de IMC ---")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# 2. Processamento (Calculo)
# A formula e Peso dividido pela Altura ao quadrado
imc = peso / (altura * altura)

# 3. Saida de Dados
# Usamos ':.2f' na f-string para mostrar apenas 2 casas decimais
print(f"Seu IMC calculado e: {imc:.2f}")