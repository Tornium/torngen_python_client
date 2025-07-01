import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .job_position_army_enum import JobPositionArmyEnum
from .job_position_casino_enum import JobPositionCasinoEnum
from .job_position_education_enum import JobPositionEducationEnum
from .job_position_grocer_enum import JobPositionGrocerEnum
from .job_position_law_enum import JobPositionLawEnum
from .job_position_medical_enum import JobPositionMedicalEnum


@dataclass
class UserJobRanks(BaseSchema):
    """
    JSON object of `UserJobRanks`.
    """

    medical: JobPositionMedicalEnum
    law: JobPositionLawEnum
    grocer: JobPositionGrocerEnum
    education: JobPositionEducationEnum
    casino: JobPositionCasinoEnum
    army: JobPositionArmyEnum

    @staticmethod
    def parse(data):
        return UserJobRanks(
            medical=BaseSchema.parse(data.get("medical"), JobPositionMedicalEnum),
            law=BaseSchema.parse(data.get("law"), JobPositionLawEnum),
            grocer=BaseSchema.parse(data.get("grocer"), JobPositionGrocerEnum),
            education=BaseSchema.parse(data.get("education"), JobPositionEducationEnum),
            casino=BaseSchema.parse(data.get("casino"), JobPositionCasinoEnum),
            army=BaseSchema.parse(data.get("army"), JobPositionArmyEnum),
        )
