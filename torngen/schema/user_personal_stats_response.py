import typing

from ..base_schema import BaseSchema
from .user_personal_stats_category import UserPersonalStatsCategory
from .user_personal_stats_full import UserPersonalStatsFull
from .user_personal_stats_full_public import UserPersonalStatsFullPublic
from .user_personal_stats_historic import UserPersonalStatsHistoric
from .user_personal_stats_popular import UserPersonalStatsPopular


class UserPersonalStatsResponse(BaseSchema):
    value: (
        UserPersonalStatsHistoric
        | UserPersonalStatsCategory
        | UserPersonalStatsPopular
        | UserPersonalStatsFullPublic
        | UserPersonalStatsFull
    )
