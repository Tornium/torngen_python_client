import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeDetailsHustling(BaseSchema):
    """
    JSON object of `UserCrimeDetailsHustling`.
    """

    total_audience_gathered: int
    shill_money_collected: int
    pickpocket_money_collected: int
    biggest_money_won: int

    @staticmethod
    def parse(data):
        return UserCrimeDetailsHustling(
            total_audience_gathered=BaseSchema.parse(
                data.get("total_audience_gathered"), int
            ),
            shill_money_collected=BaseSchema.parse(
                data.get("shill_money_collected"), int
            ),
            pickpocket_money_collected=BaseSchema.parse(
                data.get("pickpocket_money_collected"), int
            ),
            biggest_money_won=BaseSchema.parse(data.get("biggest_money_won"), int),
        )
