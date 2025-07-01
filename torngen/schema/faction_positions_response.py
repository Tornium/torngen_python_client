import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_position import FactionPosition


@dataclass
class FactionPositionsResponse(BaseSchema):
    """
    JSON object of `FactionPositionsResponse`.
    """

    positions: typing.List[FactionPosition]

    @staticmethod
    def parse(data):
        return FactionPositionsResponse(
            positions=BaseSchema.parse(
                data.get("positions"), typing.List[FactionPosition]
            ),
        )
