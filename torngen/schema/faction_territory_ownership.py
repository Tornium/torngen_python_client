import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionTerritoryOwnership(BaseSchema):
    """
    JSON object of `FactionTerritoryOwnership`.
    """

    owned_by: None | FactionId
    irradiated: bool
    id: str
    acquired_at: None | int

    @staticmethod
    def parse(data):
        return FactionTerritoryOwnership(
            owned_by=BaseSchema.parse(data.get("owned_by"), None | FactionId),
            irradiated=BaseSchema.parse(data.get("irradiated"), bool),
            id=BaseSchema.parse(data.get("id"), str),
            acquired_at=BaseSchema.parse(data.get("acquired_at"), None | int),
        )
