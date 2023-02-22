from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila: str = TIPO_FILA_NORMAL) \
            -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila.lower() == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila.lower() == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila inexistente')
