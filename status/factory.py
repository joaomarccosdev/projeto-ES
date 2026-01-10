from .status import StatusDisponivel, StatusFazendo, StatusFeita


class StatusFactory:
    """Factory para criação de status de tarefas"""
    
    def criar_status_inicial(self):
        return StatusDisponivel()
    
    def criar_status_em_andamento(self):
        return StatusFazendo()
    
    def criar_status_finalizado(self):
        return StatusFeita()