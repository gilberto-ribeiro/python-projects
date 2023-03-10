from abc import ABCMeta, abstractmethod
from typing import List

from constantes import TAMANHO_PADRAO_MINIMO, TAMANHO_PADRAO_MAXIMO


class FilaBase(metaclass=ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
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

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}. Dirija-se ao caixa: {caixa}.'

    @abstractmethod
    def gera_senha_atual(self) -> None:
        pass
