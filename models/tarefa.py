class Tarefa:
    def __init__(self, nome, descricao, status):
        if not nome or not nome.strip():
            raise ValueError("O nome da tarefa não pode estar vazio")
        if not descricao or not descricao.strip():
            raise ValueError("A descrição da tarefa não pode estar vazia")
        
        self.__nome = nome
        self.__descricao = descricao
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        self.__status = novo_status

    def __str__(self):
        return f"{self.__nome} - {self.__descricao} [{self.__status.nome()}]"
