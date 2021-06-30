# Imports do próprio módulo
from inewave._utils.bloco import Bloco
from inewave._utils.leitura import Leitura
from inewave._utils.escrita import Escrita
from inewave._utils.registros import RegistroAn
# Imports de módulos externos
from typing import IO, List
import os


class BlocoCaso(Bloco):
    """
    Bloco de informações do arquivo de
    entrada do NEWAVE `caso.dat`.
    """

    def __init__(self):

        super().__init__("",
                         "",
                         True,
                         self.le,
                         funcao_escrita=self.escreve)

        self._dados = ""

    def le(self, arq: IO):
        reg = RegistroAn(12)
        self._dados = reg.le_registro(self._linha_inicio, 0)

    def escreve(self, arq: IO):
        arq.write(self._dados)
        

class LeituraCaso(Leitura):
    """
    Realiza a leitura do arquivo `caso.dat`
    existente em um diretório de entradas do NEWAVE.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de um arquivo `caso.dat`, construindo
    um objeto `Caso` cujas informações são as mesmas do caso.dat.

    Este objeto existe para retirar do modelo de dados a complexidade
    de iterar pelas linhas do arquivo, recortar colunas, converter
    tipos de dados, dentre outras tarefas necessárias para a leitura.
    """

    def __init__(self,
                 diretorio: str):
        super().__init__(diretorio)

    # Override
    def _cria_blocos_leitura(self) -> List[Bloco]:
        """
        Cria a lista de blocos a serem lidos no arquivo caso.dat.
        """
        return [BlocoCaso()]

    # Override
    def _inicia_variaveis_leitura(self):
        """
        Inicia variáveis temporárias que são escritas durante
        a leitura do arquivo.
        """
        pass

    # Override
    def _prepara_dados_saida(self):
        """
        Trata os dados obtidos do arquivo para ser retornado.
        """
        pass