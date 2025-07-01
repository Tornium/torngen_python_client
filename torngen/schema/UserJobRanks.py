import typing

from JobPositionArmyEnum import JobPositionArmyEnum
from JobPositionCasinoEnum import JobPositionCasinoEnum
from JobPositionEducationEnum import JobPositionEducationEnum
from JobPositionGrocerEnum import JobPositionGrocerEnum
from JobPositionLawEnum import JobPositionLawEnum
from JobPositionMedicalEnum import JobPositionMedicalEnum

from ..base_schema import BaseSchema


class UserJobRanks(BaseSchema):

    medical: JobPositionMedicalEnum
    law: JobPositionLawEnum
    grocer: JobPositionGrocerEnum
    education: JobPositionEducationEnum
    casino: JobPositionCasinoEnum
    army: JobPositionArmyEnum
