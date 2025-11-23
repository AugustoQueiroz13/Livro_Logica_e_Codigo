import json
import os # Para verificar se o arquivo existe

NOME_ARQUIVO = "escola_db.json"
alunos_db = {} # Nosso banco de dados em memoria

def carregar_dados():
    """Carrega os dados do arquivo JSON se ele existir."""
    if os.path.exists(NOME_ARQUIVO):
        try:
            with open(NOME_ARQUIVO, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

def adicionar_aluno():
    print("\n--- CADASTRAR ALUNO ---")
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("Erro: O nome nao pode estar vazio.")
        return

    if nome in alunos_db:
        print("Erro: Aluno ja cadastrado.")
        return

    try:
        nota = float(input(f"Nota final de {nome}: "))
        if 0 <= nota <= 10:
            alunos_db[nome] = nota
            salvar_dados() # Salva imediatamente
            print("Sucesso: Aluno cadastrado!")
        else:
            print("Erro: A nota deve ser entre 0 e 10.")
    except ValueError:
        print("Erro: Digite um numero valido para a nota.")

def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")
    if not alunos_db:
        print("Nenhum aluno encontrado.")
    else:
        print(f"{'NOME':<20} | {'NOTA':<5}")
        print("-" * 30)
        for nome, nota in alunos_db.items():
            print(f"{nome:<20} | {nota:<5.1f}")
    print("-" * 30)

def atualizar_nota():
    print("\n--- ATUALIZAR NOTA ---")
    nome = input("Nome do aluno: ").strip()

    if nome in alunos_db:
        try:
            nova_nota = float(input(f"Nova nota para {nome}: "))
            alunos_db[nome] = nova_nota
            salvar_dados()
            print("Sucesso: Nota atualizada.")
        except ValueError:
            print("Erro: Nota invalida.")
    else:
        print("Erro: Aluno nao encontrado.")

def excluir_aluno():
    print("\n--- EXCLUIR ALUNO ---")
    nome = input("Nome do aluno a remover: ").strip()

    if nome in alunos_db:
        confirmacao = input(f"Tem certeza que deseja remover {nome}? (S/N): ")
        if confirmacao.lower() == 's':
            del alunos_db[nome]
            salvar_dados()
            print("Sucesso: Aluno removido.")
        else:
            print("Operacao cancelada.")
    else:
        print("Erro: Aluno nao encontrado.")
def menu():
    # Carrega os dados ao iniciar
    global alunos_db
    alunos_db = carregar_dados()

    while True:
        print("\n=== SISTEMA DE GESTAO ESCOLAR 2.0 ===")
        print("1. Adicionar Aluno")
        print("2. Listar Turma")
        print("3. Atualizar Nota")
        print("4. Excluir Aluno")
        print("5. Sair")

        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            atualizar_nota()
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "5":
            print("Encerrando sistema... Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()