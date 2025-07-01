import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornEducationPrerequisites(BaseSchema):
    """
    JSON object of `TornEducationPrerequisites`.
    """

    courses: typing.List[int]
    cost: int

    @staticmethod
    def parse(data):
        return TornEducationPrerequisites(
            courses=BaseSchema.parse(data.get("courses"), typing.List[int]),
            cost=BaseSchema.parse(data.get("cost"), int),
        )
