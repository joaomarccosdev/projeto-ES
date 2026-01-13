from abc import ABC, abstractmethod
from .status import StatusDisponivel, StatusFazendo, StatusFeita

class EstrategiaStatus(ABC):
    """Strategy para obtenção de status de tarefas"""
    
    @abstractmethod
    def obter_status_inicial(self):
        pass
    
    @abstractmethod
    def obter_status_em_andamento(self):
        pass
    
    @abstractmethod
    def obter_status_finalizado(self):
        pass


class EstrategiaStatusPadrao(EstrategiaStatus):
    """Estratégia padrão para criação de status"""
    
    def obter_status_inicial(self):
        return StatusDisponivel()
    
    def obter_status_em_andamento(self):
        return StatusFazendo()
    
    def obter_status_finalizado(self):
        return StatusFeita()
