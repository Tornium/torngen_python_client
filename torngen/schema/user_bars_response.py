import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_bars import UserBars


@dataclass
class UserBarsResponse(BaseSchema):
    """
    JSON object of `UserBarsResponse`.
    """

    bars: UserBars

    @staticmethod
    def parse(data):
        return UserBarsResponse(
            bars=BaseSchema.parse(data.get("bars"), UserBars),
        )
