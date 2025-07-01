import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .education_id import EducationId
from .torn_education_prerequisites import TornEducationPrerequisites
from .torn_education_rewards import TornEducationRewards


@dataclass
class TornEducationCourses(BaseSchema):
    """
    JSON object of `TornEducationCourses`.
    """

    rewards: TornEducationRewards
    prerequisites: TornEducationPrerequisites
    name: str
    id: EducationId
    duration: int
    description: str
    code: str

    @staticmethod
    def parse(data):
        return TornEducationCourses(
            rewards=BaseSchema.parse(data.get("rewards"), TornEducationRewards),
            prerequisites=BaseSchema.parse(
                data.get("prerequisites"), TornEducationPrerequisites
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), EducationId),
            duration=BaseSchema.parse(data.get("duration"), int),
            description=BaseSchema.parse(data.get("description"), str),
            code=BaseSchema.parse(data.get("code"), str),
        )
