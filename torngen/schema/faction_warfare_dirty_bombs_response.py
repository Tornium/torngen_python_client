import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_warfare_dirty_bomb import FactionWarfareDirtyBomb


@dataclass
class FactionWarfareDirtyBombsResponse(BaseSchema):
    """
    JSON object of `FactionWarfareDirtyBombsResponse`.
    """

    dirtybombs: typing.List[FactionWarfareDirtyBomb]

    @staticmethod
    def parse(data):
        return FactionWarfareDirtyBombsResponse(
            dirtybombs=BaseSchema.parse(
                data.get("dirtybombs"), typing.List[FactionWarfareDirtyBomb]
            ),
        )
