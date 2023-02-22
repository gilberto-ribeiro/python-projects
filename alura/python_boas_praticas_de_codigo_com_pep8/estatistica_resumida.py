from typing import Union, List, Dict


class EstatisticaResumida:
    def __init__(self, dia: str, agencia: int) -> None:
        self.__dia = dia
        self.__agencia = agencia

    def retorna_estatistica(self, clientes_atendidos: List[str]) \
            -> Dict[str, int]:
        estatistica: Dict[str, int] = {}
        estatistica[f'{self.__agencia}-{self.__dia}'] = (
            len(clientes_atendidos)
        )
        return estatistica
