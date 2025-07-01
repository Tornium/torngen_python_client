import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class AttackPlayerFaction(BaseSchema):
    """
    JSON object of `AttackPlayerFaction`.
    """

    name: str
    id: FactionId

    @staticmethod
    def parse(data):
        return AttackPlayerFaction(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
        )
