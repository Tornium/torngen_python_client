import typing

from FactionHofValues import FactionHofValues
from FactionId import FactionId

from ..base_schema import BaseSchema


class TornFactionHof(BaseSchema):

    values: FactionHofValues
    rank: str
    position: int
    name: str
    members: int
    id: FactionId
