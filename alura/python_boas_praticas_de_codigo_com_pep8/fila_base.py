from abc import ABCMeta, abstractmethod

from constantes import TAMANHO_PADRAO_MINIMO, TAMANHO_PADRAO_MAXIMO


class FilaBase(metaclass=ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = ''

    def atualiza_fila(self) -> None:
        # Template method.
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    @abstractmethod
    def gera_senha_atual(self) -> None:
        pass

    @abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        pass
