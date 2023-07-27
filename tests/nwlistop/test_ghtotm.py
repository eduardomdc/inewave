from inewave.nwlistop.ghtotm import Ghtotm

from datetime import datetime
from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.ghtotm import MockGhtotm

ARQ_TESTE = "./tests/mocks/arquivos/__init__.py"


def test_atributos_encontrados_ghtotm():
    m: MagicMock = mock_open(read_data="".join(MockGhtotm))
    with patch("builtins.open", m):
        n = Ghtotm.read(ARQ_TESTE)
        assert n.submercado is not None
        assert n.submercado == "SUDESTE"
        assert n.valores is not None
        assert n.valores.iloc[0, 0] == datetime(2022, 1, 1)
        assert n.valores.iloc[-1, -1] == 36951.5


def test_atributos_nao_encontrados_ghtotm():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        n = Ghtotm.read(ARQ_TESTE)
        assert n.submercado is None
        assert n.valores is None


def test_eq_ghtotm():
    m: MagicMock = mock_open(read_data="".join(MockGhtotm))
    with patch("builtins.open", m):
        n1 = Ghtotm.read(ARQ_TESTE)
        n2 = Ghtotm.read(ARQ_TESTE)
        assert n1 == n2


# Não deve ter teste de diferença, visto que o atributo é
# implementado como Lazy Property.
