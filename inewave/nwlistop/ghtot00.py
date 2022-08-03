from inewave.nwlistop.modelos.blocos.ree import REE
from inewave.nwlistop.modelos.arquivos.arquivoree import ArquivoREE
from inewave.nwlistop.modelos.ghtot00 import GHAnos


class Ghtot00(ArquivoREE):
    """
    Armazena os dados das saídas referentes à geração hidraulica total
    por patamar, por REE.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `ghtot00x.out`, onde x varia conforme o
    REE em questão.

    """

    BLOCKS = [
        REE,
        GHAnos,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="ghtot001.out"
    ) -> "Ghtot00":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="ghtot001.out"):
        self.write(diretorio, nome_arquivo)
