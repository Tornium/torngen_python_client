import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionWarfareDirtyBombTargetFaction(BaseSchema):
    """
    JSON object of `FactionWarfareDirtyBombTargetFaction`.
    """

    respect_lost: int
    name: str
    id: FactionId

    @staticmethod
    def parse(data):
        return FactionWarfareDirtyBombTargetFaction(
            respect_lost=BaseSchema.parse(data.get("respect_lost"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
        )
