import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .ranked_war_id import RankedWarId


@dataclass
class FactionRankedWarDetails(BaseSchema):
    """
    JSON object of `FactionRankedWarDetails`.
    """

    winner: None | FactionId
    target: int
    start: int
    id: RankedWarId
    factions: typing.List[
        typing.TypedDict("", {"score": int, "name": str, "id": FactionId, "chain": int})
    ]
    end: int

    @staticmethod
    def parse(data):
        return FactionRankedWarDetails(
            winner=BaseSchema.parse(data.get("winner"), None | FactionId),
            target=BaseSchema.parse(data.get("target"), int),
            start=BaseSchema.parse(data.get("start"), int),
            id=BaseSchema.parse(data.get("id"), RankedWarId),
            factions=BaseSchema.parse(
                data.get("factions"),
                typing.List[
                    typing.TypedDict(
                        "", {"score": int, "name": str, "id": FactionId, "chain": int}
                    )
                ],
            ),
            end=BaseSchema.parse(data.get("end"), int),
        )
