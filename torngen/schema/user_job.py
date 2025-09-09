import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .job_position_army_enum import JobPositionArmyEnum
from .job_position_casino_enum import JobPositionCasinoEnum
from .job_position_education_enum import JobPositionEducationEnum
from .job_position_grocer_enum import JobPositionGrocerEnum
from .job_position_law_enum import JobPositionLawEnum
from .job_position_medical_enum import JobPositionMedicalEnum
from .job_type_enum import JobTypeEnum


@dataclass
class UserJob(BaseSchema):
    """
    JSON object of `UserJob`.
    """

    type: typing.Literal["job"]
    position: (
        JobPositionEducationEnum
        | JobPositionLawEnum
        | JobPositionMedicalEnum
        | JobPositionCasinoEnum
        | JobPositionGrocerEnum
        | JobPositionArmyEnum
    )
    name: JobTypeEnum

    @staticmethod
    def parse(data):
        return UserJob(
            type=BaseSchema.parse(data.get("type"), typing.Literal["job"]),
            position=BaseSchema.parse(
                data.get("position"),
                JobPositionEducationEnum
                | JobPositionLawEnum
                | JobPositionMedicalEnum
                | JobPositionCasinoEnum
                | JobPositionGrocerEnum
                | JobPositionArmyEnum,
            ),
            name=BaseSchema.parse(data.get("name"), JobTypeEnum),
        )
