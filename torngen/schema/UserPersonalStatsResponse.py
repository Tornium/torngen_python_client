import typing

from UserPersonalStatsCategory import UserPersonalStatsCategory
from UserPersonalStatsFull import UserPersonalStatsFull
from UserPersonalStatsFullPublic import UserPersonalStatsFullPublic
from UserPersonalStatsHistoric import UserPersonalStatsHistoric
from UserPersonalStatsPopular import UserPersonalStatsPopular

from ..base_schema import BaseSchema


class UserPersonalStatsResponse(BaseSchema):
    value: (
        UserPersonalStatsHistoric
        | UserPersonalStatsCategory
        | UserPersonalStatsPopular
        | UserPersonalStatsFullPublic
        | UserPersonalStatsFull
    )
