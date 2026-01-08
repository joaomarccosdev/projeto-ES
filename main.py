from models.tarefa import Tarefa
from services.gerenciador import GerenciadorTarefas
from status.status import Disponivel, Fazendo, Feita

STATUS_OPTIONS = {
    "1": Disponivel,
    "2": Fazendo,
    "3": Feita,
}

def mostrar_menu():
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Alterar status")
    print("0 - Sair")

def adicionar_tarefa(gerenciador):
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return

    descricao = input("Descrição: ").strip()
    tarefa = Tarefa(nome, descricao, Disponivel())
    gerenciador.adicionar(tarefa)
    print("A Tarefa adicionada com êxito.")

def listar_tarefas(gerenciador):
    tarefas = gerenciador.listar()
    if not tarefas:
        print("Nenhuma tarefa foi cadastrada ainda.")
        return main ()

    for i, tarefa in enumerate(tarefas):
        print(f"{i} - {tarefa}")

def remover_tarefa(gerenciador):
    listar_tarefas(gerenciador)
    try:
        indice = int(input("Índice da tarefa a remover: "))
        gerenciador.remover(indice)
        print("Tarefa removida da lista.")
    except (ValueError, IndexError):
        print("Índice inválido. Repita a operação")

def alterar_status(gerenciador):
    listar_tarefas(gerenciador)
    try:
        indice = int(input("Índice da tarefa: "))
        print("\n1 - Disponível \n2 - Fazendo \n3 - Feita")
        opcao = input("Novo status: ").strip()

        status_cls = STATUS_OPTIONS.get(opcao)
        if not status_cls:
            print("Opção de status inválida.")
            return

        gerenciador.alterar_status(indice, status_cls())
        print("Status atualizado.")
    except (ValueError, IndexError):
        print("Índice inválido.")

def main():
    gerenciador = GerenciadorTarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_tarefa(gerenciador)
        elif opcao == "2":
            listar_tarefas(gerenciador)
        elif opcao == "3":
            remover_tarefa(gerenciador)
        elif opcao == "4":
            alterar_status(gerenciador)
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
