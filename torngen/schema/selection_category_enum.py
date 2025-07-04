import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .personal_stats_category_enum import PersonalStatsCategoryEnum
from .racing_race_type_enum import RacingRaceTypeEnum
from .report_type_enum import ReportTypeEnum
from .user_list_enum import UserListEnum


@dataclass
class SelectionCategoryEnum(BaseSchema):
    value: (
        RacingRaceTypeEnum | PersonalStatsCategoryEnum | UserListEnum | ReportTypeEnum
    )
