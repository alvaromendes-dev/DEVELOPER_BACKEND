import json
import os

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)


def listar_tarefas(tarefas):
    if not tarefas:
        print("\n📭 Nenhuma tarefa encontrada.\n")
        return
    print("\n📋 Suas Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {tarefa['titulo']} [{status}]")
    print()


def adicionar_tarefa(tarefas):
    titulo = input("Digite o nome da nova tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!\n")


def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Número da tarefa para marcar como concluída: ")) - 1
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!\n")
    except (IndexError, ValueError):
        print("Número inválido!\n")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Número da tarefa para remover: ")) - 1
        tarefa_removida = tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa_removida['titulo']}' removida!\n")
    except (IndexError, ValueError):
        print("Número inválido!\n")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("=== GERENCIADOR DE TAREFAS ===")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    menu()
