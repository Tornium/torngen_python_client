import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionRaidWarParticipant(BaseSchema):

    score: int
    name: str
    is_aggressor: bool
    id: FactionId
    chain: int
