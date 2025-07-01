import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornSubcrime(BaseSchema):
    """
    JSON object of `TornSubcrime`.
    """

    nerve_cost: int
    name: str
    id: int

    @staticmethod
    def parse(data):
        return TornSubcrime(
            nerve_cost=BaseSchema.parse(data.get("nerve_cost"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), int),
        )
