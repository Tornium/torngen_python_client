import typing

from EducationId import EducationId
from TornEducationPrerequisites import TornEducationPrerequisites
from TornEducationRewards import TornEducationRewards

from ..base_schema import BaseSchema


class TornEducationCourses(BaseSchema):

    rewards: TornEducationRewards
    prerequisites: TornEducationPrerequisites
    name: str
    id: EducationId
    duration: int
    description: str
    code: str
