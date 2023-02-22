from typing import Union, List, Dict

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def estatistica(self, dia: str, agencia: int, classe_estatistica) \
            -> Dict[str, Union[int, str, List[str]]]:
        estatistica = classe_estatistica(dia, agencia)
        return estatistica.retorna_estatistica(self.clientes_atendidos)
