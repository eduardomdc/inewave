from inewave.nwlistop.modelos.blocos.usina import Usina
from inewave.nwlistop.modelos.arquivos.arquivousinapatamar import (
    ArquivoUsinaPatamar,
)
from inewave.nwlistop.modelos.vturuh import VturAnos

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Vturuh(ArquivoUsinaPatamar):
    """
    Armazena os dados das saídas referentes às vazões turbinadas por usina.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `vturuh00x.out`, onde x varia conforme a
    usina em questão.

    """

    BLOCKS = [
        Usina,
        VturAnos,
    ]
