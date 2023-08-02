from inewave.nwlistop.modelos.blocos.ree import REE
from inewave.nwlistop.modelos.arquivos.arquivoree import ArquivoREE
from inewave.nwlistop.modelos.perdf import PerdfAnos

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Perdf(ArquivoREE):
    """
    Armazena os dados das saídas referentes ao vertimento fio d'água
    , por REE.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `perdf00x.out`, onde x varia conforme o
    REE em questão.

    """

    BLOCKS = [
        REE,
        PerdfAnos,
    ]
