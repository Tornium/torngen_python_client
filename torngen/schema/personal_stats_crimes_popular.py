import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsCrimesPopular(BaseSchema):
    """
    JSON object of `PersonalStatsCrimesPopular`.
    """

    crimes: typing.TypedDict("", {"version": str, "total": int})

    @staticmethod
    def parse(data):
        return PersonalStatsCrimesPopular(
            crimes=BaseSchema.parse(
                data.get("crimes"), typing.TypedDict("", {"version": str, "total": int})
            ),
        )
