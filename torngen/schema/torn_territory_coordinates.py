import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornTerritoryCoordinates(BaseSchema):
    """
    JSON object of `TornTerritoryCoordinates`.
    """

    y: int | float
    x: int | float

    @staticmethod
    def parse(data):
        return TornTerritoryCoordinates(
            y=BaseSchema.parse(data.get("y"), int | float),
            x=BaseSchema.parse(data.get("x"), int | float),
        )
