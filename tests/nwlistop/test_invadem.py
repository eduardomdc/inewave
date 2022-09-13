from inewave.nwlistop.invadem import Invadem

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.invadem import MockInvadem


def test_atributos_encontrados_invadem():
    m: MagicMock = mock_open(read_data="".join(MockInvadem))
    with patch("builtins.open", m):
        n = Invadem.le_arquivo("")
        assert n.valores is not None
        assert n.valores.iloc[0, 0] == 2020
        assert n.valores.iloc[-1, -1] == 0.0


def test_atributos_nao_encontrados_invadem():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        n = Invadem.le_arquivo("")
        assert n.valores is None


def test_eq_invadem():
    m: MagicMock = mock_open(read_data="".join(MockInvadem))
    with patch("builtins.open", m):
        n1 = Invadem.le_arquivo("")
        n2 = Invadem.le_arquivo("")
        assert n1 == n2


# Não deve ter teste de diferença, visto que o atributo é
# implementado como Lazy Property.