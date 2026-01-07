class GerenciadorTarefas:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._tarefas = []
        return cls._instancia

    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)

    def listar(self):
        return self._tarefas

    def remover(self, indice):
        self._tarefas.pop(indice)

    def obter(self, indice):
        return self._tarefas[indice]

    def alterar_status(self, indice, novo_status):
        self._tarefas[indice].status = novo_status
