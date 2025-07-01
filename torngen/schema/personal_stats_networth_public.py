import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsNetworthPublic(BaseSchema):
    """
    JSON object of `PersonalStatsNetworthPublic`.
    """

    networth: typing.TypedDict("", {"total": int})

    @staticmethod
    def parse(data):
        return PersonalStatsNetworthPublic(
            networth=BaseSchema.parse(
                data.get("networth"), typing.TypedDict("", {"total": int})
            ),
        )
