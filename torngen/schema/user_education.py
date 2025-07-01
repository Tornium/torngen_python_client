import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .education_id import EducationId
from .user_current_education import UserCurrentEducation


@dataclass
class UserEducation(BaseSchema):
    """
    JSON object of `UserEducation`.
    """

    current: None | UserCurrentEducation
    complete: typing.List[EducationId]

    @staticmethod
    def parse(data):
        return UserEducation(
            current=BaseSchema.parse(data.get("current"), None | UserCurrentEducation),
            complete=BaseSchema.parse(data.get("complete"), typing.List[EducationId]),
        )
