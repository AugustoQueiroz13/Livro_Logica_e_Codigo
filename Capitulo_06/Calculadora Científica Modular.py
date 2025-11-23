import math

# 1. Definindo as funcoes puras
def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    return "Erro: Divisao por zero" if b == 0 else a / b
def potencia(a, b): return a ** b

# 2. Mapeando strings para funcoes (O segredo!)
operacoes = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
    "^": potencia
 }

def calculadora():
    print("--- Calculadora Modular ---")
    print("Operacoes disponiveis:", list(operacoes.keys())
)

    while True:
        op = input("\nEscolha a operacao (ou 'sair'): ")
        if op == 'sair': break

        if op in operacoes:
            try:
                n1 = float(input("Numero 1: "))
                n2 = float(input("Numero 2: "))

                # Busca a funcao no dicionario e executa
                funcao_escolhida = operacoes[op]
                resultado = funcao_escolhida(n1, n2)

                print(f"Resultado: {resultado}")
            except ValueError:
                print("Erro: Digite apenas numeros validos.")
        else:
            print("Operacao invalida.")
# Executar
calculadora()