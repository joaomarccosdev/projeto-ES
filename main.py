from services.gerenciador import GerenciadorTarefas
from status.estrategia import EstrategiaStatusPadrao
from interface.interface import InterfaceUsuario

def main():
    gerenciador = GerenciadorTarefas()
    estrategia = EstrategiaStatusPadrao()
    interface = InterfaceUsuario(gerenciador, estrategia)
    interface.executar()

if __name__ == "__main__":
    main()
