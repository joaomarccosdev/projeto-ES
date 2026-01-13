class GerenciadorTarefas:
 
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.__tarefas = []
        return cls._instancia
    
    def adicionar(self, tarefa):
     
        self.__tarefas.append(tarefa)
    
    def listar(self):
     
        return self.__tarefas.copy()
    
    def remover(self, indice):
        
        if not self._indice_valido(indice):
            raise IndexError("Índice inválido")
        self.__tarefas.pop(indice)
    
    def obter_tarefa(self, indice):
       
        if not self._indice_valido(indice):
            raise IndexError("Índice inválido")
        return self.__tarefas[indice]
    
    def alterar_status(self, indice, novo_status):
        
        if not self._indice_valido(indice):
            raise IndexError("Índice inválido")
        self.__tarefas[indice].status = novo_status
    
    def _indice_valido(self, indice):
       
        return 0 <= indice < len(self.__tarefas)
    
    def total_tarefas(self):
       
        return len(self.__tarefas)