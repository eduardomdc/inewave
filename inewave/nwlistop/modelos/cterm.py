from inewave.config import MESES_DF

from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField
from inewave.nwlistop.modelos.blocos.valoresseriepatamar import (
    ValoresSeriePatamar,
)


class CtermsAnos(ValoresSeriePatamar):
    """
    Bloco com a informaçao do submercado associado aos valores de custo
    de geração térmica.
    """

    HEADER_LINE = Line([IntegerField(4, 10)])
    DATA_LINE = Line(
        [  # type: ignore
            IntegerField(4, 2),
            IntegerField(2, 9),
        ]
        + [FloatField(9, 13 + 10 * i, 2) for i in range(len(MESES_DF) + 1)]  # type: ignore
    )