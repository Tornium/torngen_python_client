import typing

from ..base_schema import BaseSchema


class TornItemBaseStats(BaseSchema):

    damage: int
    armor: int
    accuracy: int
