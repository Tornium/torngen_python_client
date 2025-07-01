import typing

from TornEducationCourses import TornEducationCourses

from ..base_schema import BaseSchema


class TornEducation(BaseSchema):

    name: str
    id: int
    courses: typing.List[TornEducationCourses]
