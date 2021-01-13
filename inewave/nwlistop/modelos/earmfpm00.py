from typing import Dict
import numpy as np  # type: ignore
from inewave.config import NUM_CENARIOS, MESES


class Earmfpm00:
    """
    Classe responsável por lidar com o armazenamento dos dados das
    saídas do NWListOP referentes às energias armazenadas finais,
    por submercado e em % da energia armazenável máxima:
    earmfpm00x.out.
    """
    def __init__(self,
                 mes_pmo: int,
                 ano_pmo: int,
                 versao_newave: str,
                 submercado: str,
                 energias_armazenadas: Dict[int,
                                            np.ndarray]):
        self.mes_pmo = mes_pmo
        self.ano_pmo = ano_pmo
        self.versao_newave = versao_newave
        self.submercado = submercado
        self.energias_armazenadas = energias_armazenadas

    @property
    def energias_por_ano(self) -> Dict[int, np.ndarray]:
        """
        Retorna as energias armazenadas para cada ano e em cada cenário, para
        todos os meses, organizadas primeiramente por ano. O acesso é feito
        com [ano] e retorna um np.ndarray com os valores de EARM para todos os
        cenários e meses, naquele ano.
        """
        return self.energias_armazenadas

    @property
    def energias_por_ano_e_mes(self) -> Dict[int,
                                             Dict[int, np.ndarray]]:
        """
        Retorna as energias armazenadas para cada ano e mês em cada cenário,
        para todos os meses, organizadas primeiramente por ano. O acesso é
        feito com [ano][mes] e retorna um np.ndarray com os valores de EARM
        para todos os cenários, naquele ano e mês.
        """
        energias: Dict[int,
                       Dict[int, np.ndarray]] = {}
        anos_estudo = list(self.energias_armazenadas.keys())
        n_meses = len(MESES)
        # Cria e inicializa os objetos a serem retornados
        for a in anos_estudo:
            energias[a] = {m: []
                           for m in range(1, n_meses + 1)}
        # Preenche com os valores
        for a, tabela in self.energias_armazenadas.items():
            for m in range(1, n_meses + 1):
                col = m - 1
                energias[a][m] = tabela[:, col]
        return energias

    @property
    def energias_por_ano_e_cenario(self) -> Dict[int,
                                                 Dict[int, np.ndarray]]:
        """
        Retorna as energias armazenadas para cada ano e cenário, para todos os
        meses, organizadas primeiramente por ano. O acesso é feito
        com [ano][cenario] e retorna um np.ndarray com os valores de EARM para
        todos os meses, naquele ano e cenário.
        """
        energias: Dict[int,
                       Dict[int, np.ndarray]] = {}
        anos_estudo = list(self.energias_armazenadas.keys())
        # Cria e inicializa os objetos a serem retornados
        for a in anos_estudo:
            energias[a] = {c: []
                           for c in range(NUM_CENARIOS)}
        # Preenche com os valores
        for a, tabela in self.energias_armazenadas.items():
            for c in range(NUM_CENARIOS):
                energias[a][c] = tabela[c, :]
        return energias