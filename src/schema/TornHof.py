import typing

from FactionId import FactionId
from UserId import UserId

from ..base_schema import BaseSchema


class TornHof(BaseSchema):

    value: typing.Any
    username: str
    signed_up: int
    rank_number: int
    rank_name: str
    rank: str
    position: int
    level: int
    last_action: int
    id: UserId
    faction_id: FactionId
    age_in_days: int
