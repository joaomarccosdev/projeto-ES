class Tarefa:
    def __init__(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        self.status = status

    def __str__(self):
        return f"{self.nome} - {self.descricao} [{self.status.nome()}]"