import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsTravelPopular(BaseSchema):
    """
    JSON object of `PersonalStatsTravelPopular`.
    """

    travel: typing.TypedDict("", {"total": int, "time_spent": int})

    @staticmethod
    def parse(data):
        return PersonalStatsTravelPopular(
            travel=BaseSchema.parse(
                data.get("travel"),
                typing.TypedDict("", {"total": int, "time_spent": int}),
            ),
        )
