from models.tarefa import Tarefa
from services.gerenciador import GerenciadorTarefas
from status.status import Disponivel, Fazendo, Feita

gerenciador = GerenciadorTarefas()

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Alterar status")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        desc = input("Descrição: ")
        tarefa = Tarefa(nome, desc, Disponivel())
        gerenciador.adicionar(tarefa)

    elif opcao == "2":
        for i, t in enumerate(gerenciador.listar()):
            print(f"{i} - {t}")

    elif opcao == "3":
        i = int(input("Índice da tarefa: "))
        gerenciador.remover(i)

    elif opcao == "4":
        i = int(input("Índice da tarefa: "))
        print("1- Disponível | 2- Fazendo | 3- Feita")
        s = input("Novo status: ")

        if s == "1":
            gerenciador.tarefas[i].status = Disponivel()
        elif s == "2":
            gerenciador.tarefas[i].status = Fazendo()
        elif s == "3":
            gerenciador.tarefas[i].status = Feita()

    elif opcao == "0":
        break

