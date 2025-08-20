import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_skill_slug_enum import UserSkillSlugEnum


@dataclass
class UserSkillDetail(BaseSchema):
    """
    JSON object of `UserSkillDetail`.
    """

    slug: str | UserSkillSlugEnum
    name: str
    level: int | float

    @staticmethod
    def parse(data):
        return UserSkillDetail(
            slug=BaseSchema.parse(data.get("slug"), str | UserSkillSlugEnum),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int | float),
        )
