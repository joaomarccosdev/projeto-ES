class GerenciadorTarefas:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.tarefas = []
        return cls._instancia

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def listar(self):
        return self.tarefas

    def remover(self, indice):
        self.tarefas.pop(indice)
