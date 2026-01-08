class Status:
    def nome(self):
        pass


class Disponivel(Status):
    def nome(self):
        return "Disponível"


class Fazendo(Status):
    def nome(self):
        return "Fazendo"


class Feita(Status):
    def nome(self):
        return "Feita"
