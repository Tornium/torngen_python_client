import typing

from FactionId import FactionId
from RankedWarId import RankedWarId

from ..base_schema import BaseSchema


class FactionRankedWarDetails(BaseSchema):

    winner: None | FactionId
    target: int
    start: int
    id: RankedWarId
    factions: typing.List[
        typing.TypedDict("", {"score": int, "name": str, "id": FactionId, "chain": int})
    ]
    end: int
