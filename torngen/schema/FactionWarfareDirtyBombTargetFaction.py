import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionWarfareDirtyBombTargetFaction(BaseSchema):

    respect_lost: int
    name: str
    id: FactionId
