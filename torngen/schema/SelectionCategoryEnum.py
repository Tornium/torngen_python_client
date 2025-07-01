import typing

from PersonalStatsCategoryEnum import PersonalStatsCategoryEnum
from RacingRaceTypeEnum import RacingRaceTypeEnum
from ReportTypeEnum import ReportTypeEnum
from UserListEnum import UserListEnum

from ..base_schema import BaseSchema


class SelectionCategoryEnum(BaseSchema):
    value: (
        RacingRaceTypeEnum | PersonalStatsCategoryEnum | UserListEnum | ReportTypeEnum
    )
