from typing import Union, List, Dict


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.__dia = dia
        self.__agencia = agencia

    def retorna_estatistica(self, clientes_atendidos: List[str]) \
            -> Dict[str, Union[int, str, List[str]]]:
        estatistica: Dict[str, Union[int, str, List[str]]] = {}
        estatistica['dia'] = self.__dia
        estatistica['agencia'] = self.__agencia
        estatistica['clientes_atendidos'] = clientes_atendidos
        estatistica['quantidade_clientes_atendidos'] = (
            len(clientes_atendidos)
        )
        return estatistica
