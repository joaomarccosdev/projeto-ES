

from services.gerenciador import GerenciadorTarefas
from status.factory import StatusFactory
from interface.interface_usuario import InterfaceUsuario


def main():
    
    gerenciador = GerenciadorTarefas()
    factory = StatusFactory()
    interface = InterfaceUsuario(gerenciador, factory)
    
    interface.executar()


if __name__ == "__main__":
    main()