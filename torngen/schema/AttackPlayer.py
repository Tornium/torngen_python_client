import typing

from AttackPlayerFaction import AttackPlayerFaction
from UserId import UserId

from ..base_schema import BaseSchema


class AttackPlayer(BaseSchema):

    name: str
    level: int
    id: UserId
    faction: None | AttackPlayerFaction
