import typing

from UserId import UserId

from ..base_schema import BaseSchema


class AttackLogSummary(BaseSchema):

    name: None | str
    misses: int
    id: None | UserId
    hits: int
    damage: int
