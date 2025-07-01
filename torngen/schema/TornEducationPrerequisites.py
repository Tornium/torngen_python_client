import typing

from ..base_schema import BaseSchema


class TornEducationPrerequisites(BaseSchema):

    courses: typing.List[int]
    cost: int
