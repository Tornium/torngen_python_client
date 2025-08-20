import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_skill_detail import UserSkillDetail


@dataclass
class UserSkillsResponse(BaseSchema):
    """
    JSON object of `UserSkillsResponse`.
    """

    skills: typing.List[UserSkillDetail]

    @staticmethod
    def parse(data):
        return UserSkillsResponse(
            skills=BaseSchema.parse(data.get("skills"), typing.List[UserSkillDetail]),
        )
