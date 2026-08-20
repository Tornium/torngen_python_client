import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class FactionCrimeExpResponse(BaseSchema):
    """
    JSON object of `FactionCrimeExpResponse`.
    """

    crimeexp: typing.List[UserId]

    @staticmethod
    def parse(data):
        return FactionCrimeExpResponse(
            crimeexp=BaseSchema.parse(data.get("crimeexp"), typing.List[UserId]),
        )
