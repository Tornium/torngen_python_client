import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_hof_values import FactionHofValues
from .faction_id import FactionId


@dataclass
class TornFactionHof(BaseSchema):
    """
    JSON object of `TornFactionHof`.
    """

    values: FactionHofValues
    rank: str
    position: int
    name: str
    members: int
    id: FactionId

    @staticmethod
    def parse(data):
        return TornFactionHof(
            values=BaseSchema.parse(data.get("values"), FactionHofValues),
            rank=BaseSchema.parse(data.get("rank"), str),
            position=BaseSchema.parse(data.get("position"), int),
            name=BaseSchema.parse(data.get("name"), str),
            members=BaseSchema.parse(data.get("members"), int),
            id=BaseSchema.parse(data.get("id"), FactionId),
        )
