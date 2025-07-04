import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornOrganizedCrimeSpawn(BaseSchema):
    """
    JSON object of `TornOrganizedCrimeSpawn`.
    """

    name: str
    level: int

    @staticmethod
    def parse(data):
        return TornOrganizedCrimeSpawn(
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
        )
