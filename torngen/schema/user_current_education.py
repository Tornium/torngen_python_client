import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .education_id import EducationId


@dataclass
class UserCurrentEducation(BaseSchema):
    """
    JSON object of `UserCurrentEducation`.
    """

    until: int
    id: EducationId

    @staticmethod
    def parse(data):
        return UserCurrentEducation(
            until=BaseSchema.parse(data.get("until"), int),
            id=BaseSchema.parse(data.get("id"), EducationId),
        )
