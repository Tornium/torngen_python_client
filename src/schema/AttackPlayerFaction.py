import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class AttackPlayerFaction(BaseSchema):

    name: str
    id: FactionId
