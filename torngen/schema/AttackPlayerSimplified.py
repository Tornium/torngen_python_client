import typing

from FactionId import FactionId
from UserId import UserId

from ..base_schema import BaseSchema


class AttackPlayerSimplified(BaseSchema):

    id: UserId
    faction_id: None | FactionId
