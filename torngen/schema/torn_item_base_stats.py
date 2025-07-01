import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornItemBaseStats(BaseSchema):
    """
    JSON object of `TornItemBaseStats`.
    """

    damage: int
    armor: int
    accuracy: int

    @staticmethod
    def parse(data):
        return TornItemBaseStats(
            damage=BaseSchema.parse(data.get("damage"), int),
            armor=BaseSchema.parse(data.get("armor"), int),
            accuracy=BaseSchema.parse(data.get("accuracy"), int),
        )
