from abc import ABCMeta, abstractmethod


class FilaBase(metaclass=ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
    # O método gera_senha_atual() é definido nas classes filhas.
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    @abstractmethod
    def gera_senha_atual(self):
        pass

    @abstractmethod
    def chama_cliente(self, caixa):
        pass
