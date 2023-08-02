from inewave.nwlistop.modelos.blocos.submercado import Submercado
from inewave.nwlistop.modelos.merclsin import MerclAnos

from inewave.nwlistop.modelos.arquivos.arquivosubmercado import (
    ArquivoSubmercado,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Mercl(ArquivoSubmercado):
    """
    Armazena os dados das saídas referentes ao mercado líquido
    de cada estágio em cada série por submercado.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `mercl001.out`.
    """

    BLOCKS = [
        Submercado,
        MerclAnos,
    ]
