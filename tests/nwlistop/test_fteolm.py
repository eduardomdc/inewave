from inewave.nwlistop.fteolm import Fteolm

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.fteolm import MockFteolm


def test_atributos_encontrados_fteolm():
    m: MagicMock = mock_open(read_data="".join(MockFteolm))
    with patch("builtins.open", m):
        n = Fteolm.le_arquivo("")
        assert n.submercado is not None
        assert n.submercado == "SUDESTE"
        assert n.valores is not None
        assert n.valores.iloc[0, 0] == 2020
        assert n.valores.iloc[-1, -1] == 0.0


def test_atributos_nao_encontrados_fteolm():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        n = Fteolm.le_arquivo("")
        assert n.submercado is None
        assert n.valores is None


def test_eq_fteolm():
    m: MagicMock = mock_open(read_data="".join(MockFteolm))
    with patch("builtins.open", m):
        n1 = Fteolm.le_arquivo("")
        n2 = Fteolm.le_arquivo("")
        assert n1 == n2


# Não deve ter teste de diferença, visto que o atributo é
# implementado como Lazy Property.