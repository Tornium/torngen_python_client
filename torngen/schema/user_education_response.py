import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_education import UserEducation


@dataclass
class UserEducationResponse(BaseSchema):
    """
    JSON object of `UserEducationResponse`.
    """

    education: UserEducation

    @staticmethod
    def parse(data):
        return UserEducationResponse(
            education=BaseSchema.parse(data.get("education"), UserEducation),
        )
