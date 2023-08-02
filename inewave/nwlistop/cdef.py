from inewave.nwlistop.modelos.cdef import CdefAnos

from inewave.nwlistop.modelos.arquivos.arquivosubmercado import (
    ArquivoSubmercado,
    Submercado,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Cdef(ArquivoSubmercado):
    """
    Armazena os dados das saídas referentes ao custo de déficit
    de cada estágio em cada série.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `cdef00x.out`.
    """

    BLOCKS = [CdefAnos, Submercado]
