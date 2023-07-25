from cfinterface.files.sectionfile import SectionFile
from inewave.newave.modelos.vazaob import SecaoDadosVazaob
import pandas as pd  # type: ignore

from typing import TypeVar, Optional

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Vazaob(SectionFile):
    """
    Armazena os dados de saída do NEWAVE referentes às séries sintéticas
    de vazão para a etapa backward geradas pelo modelo.
    """

    T = TypeVar("T")

    SECTIONS = [SecaoDadosVazaob]
    STORAGE = "BINARY"

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls,
        diretorio: str,
        nome_arquivo="vazaob.dat",
        numero_forwards: int = 200,
        numero_aberturas: int = 20,
        numero_uhes: int = 164,
        numero_estagios: int = 60,
    ) -> "Vazaob":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(
            join(diretorio, nome_arquivo),
            numero_forwards=numero_forwards,
            numero_aberturas=numero_aberturas,
            numero_uhes=numero_uhes,
            numero_estagios=numero_estagios,
        )

    @property
    def series(self) -> Optional[pd.DataFrame]:
        """
        Obtém a tabela com os dados das séries de vazão
        afluente por UHE, por estágio, série forward e abertura.

        - estagio (`int`): estágio do cenário gerado
        - uhe (`int`): UHE para a qual foi gerado
        - serie (`int`): índice da série forward
        - abertura (`int`): índice da abertura
        - valor (`float`): energia em MWmes

        :return: A tabela com os dados das séries
        :rtype: pd.DataFrame | None
        """
        sections = [r for r in self.data.of_type(SecaoDadosVazaob)]
        if len(sections) > 0:
            return sections[0].data
        else:
            return None

    @series.setter
    def series(self, df: pd.DataFrame):
        sections = [r for r in self.data.of_type(SecaoDadosVazaob)]
        if len(sections) > 0:
            sections[0].data = df