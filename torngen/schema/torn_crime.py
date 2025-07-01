import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_crime_id import TornCrimeId


@dataclass
class TornCrime(BaseSchema):
    """
    JSON object of `TornCrime`.
    """

    unique_outcomes_ids: typing.List[int]
    unique_outcomes_count: int
    notes: typing.List[str]
    name: str
    id: TornCrimeId
    enhancer_name: str
    enhancer_id: int
    category_name: str
    category_id: int

    @staticmethod
    def parse(data):
        return TornCrime(
            unique_outcomes_ids=BaseSchema.parse(
                data.get("unique_outcomes_ids"), typing.List[int]
            ),
            unique_outcomes_count=BaseSchema.parse(
                data.get("unique_outcomes_count"), int
            ),
            notes=BaseSchema.parse(data.get("notes"), typing.List[str]),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), TornCrimeId),
            enhancer_name=BaseSchema.parse(data.get("enhancer_name"), str),
            enhancer_id=BaseSchema.parse(data.get("enhancer_id"), int),
            category_name=BaseSchema.parse(data.get("category_name"), str),
            category_id=BaseSchema.parse(data.get("category_id"), int),
        )
