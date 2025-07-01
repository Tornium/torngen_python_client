import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_education_courses import TornEducationCourses


@dataclass
class TornEducation(BaseSchema):
    """
    JSON object of `TornEducation`.
    """

    name: str
    id: int
    courses: typing.List[TornEducationCourses]

    @staticmethod
    def parse(data):
        return TornEducation(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), int),
            courses=BaseSchema.parse(
                data.get("courses"), typing.List[TornEducationCourses]
            ),
        )
