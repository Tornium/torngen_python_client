import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornOrganizedCrimeScope(BaseSchema):
    """
    JSON object of `TornOrganizedCrimeScope`.
    """

    return_: int
    cost: int

    @staticmethod
    def parse(data):
        return TornOrganizedCrimeScope(
            return_=BaseSchema.parse(data.get("return"), int),
            cost=BaseSchema.parse(data.get("cost"), int),
        )
