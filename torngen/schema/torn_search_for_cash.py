import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_sub_crime_id import TornSubCrimeId


@dataclass
class TornSearchForCash(BaseSchema):
    """
    JSON object of `TornSearchForCash`.
    """

    title: str
    percentage: int
    id: TornSubCrimeId

    @staticmethod
    def parse(data):
        return TornSearchForCash(
            title=BaseSchema.parse(data.get("title"), str),
            percentage=BaseSchema.parse(data.get("percentage"), int),
            id=BaseSchema.parse(data.get("id"), TornSubCrimeId),
        )
