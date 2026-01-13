from models.tarefa import Tarefa

class InterfaceUsuario:
    def __init__(self, gerenciador, estrategia):
        self.__gerenciador = gerenciador
        self.__estrategia = estrategia

    def exibir_menu(self):
        print("\n" + "="*40)
        print("SISTEMA DE GERENCIAMENTO DE TAREFAS")
        print("="*40)
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Alterar status")
        print("0 - Sair")
        print("="*40)

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self._adicionar_tarefa()
            elif opcao == "2":
                self._listar_tarefas()
            elif opcao == "3":
                self._remover_tarefa()
            elif opcao == "4":
                self._alterar_status()
            elif opcao == "0":
                break

    def _adicionar_tarefa(self):
        nome = input("Nome da tarefa: ").strip()
        descricao = input("Descrição: ").strip()
        status = self.__estrategia.obter_status_inicial()
        tarefa = Tarefa(nome, descricao, status)
        self.__gerenciador.adicionar(tarefa)

    def _listar_tarefas(self):
        for i, tarefa in enumerate(self.__gerenciador.listar()):
            print(f"{i} - {tarefa}")

    def _remover_tarefa(self):
        self._listar_tarefas()
        indice = int(input("Índice da tarefa a remover: "))
        self.__gerenciador.remover(indice)

    def _alterar_status(self):
        self._listar_tarefas()
        indice = int(input("Índice da tarefa: "))
        print("1 - Disponível")
        print("2 - Fazendo")
        print("3 - Feita")
        opcao = input("Opção: ")
        
        if opcao == "1":
            status = self.__estrategia.obter_status_inicial()
        elif opcao == "2":
            status = self.__estrategia.obter_status_em_andamento()
        elif opcao == "3":
            status = self.__estrategia.obter_status_finalizado()
        else:
            return
        
        self.__gerenciador.alterar_status(indice, status)