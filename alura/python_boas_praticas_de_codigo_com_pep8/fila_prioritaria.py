from typing import Union, List, Dict

from fila_base import FilaBase
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
from constantes import CODIGO_PRIORITARIO

ClassesEstatistica = Union[EstatisticaDetalhada, EstatisticaResumida]
Estatistica = Union[Dict[str, Union[int, str, List[str]]], Dict[str, int]]


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def estatistica(self, classe_estatistica: ClassesEstatistica) \
            -> Estatistica:
        return classe_estatistica.retorna_estatistica(self.clientes_atendidos)
