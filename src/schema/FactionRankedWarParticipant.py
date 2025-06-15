import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionRankedWarParticipant(BaseSchema):

    score: int
    name: str
    id: FactionId
    chain: int
