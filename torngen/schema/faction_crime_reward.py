import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_reward_item import FactionCrimeRewardItem
from .faction_crime_reward_payout import FactionCrimeRewardPayout


@dataclass
class FactionCrimeReward(BaseSchema):
    """
    JSON object of `FactionCrimeReward`.
    """

    scope: int
    respect: int
    payout: None | FactionCrimeRewardPayout
    money: int
    items: typing.List[FactionCrimeRewardItem]

    @staticmethod
    def parse(data):
        return FactionCrimeReward(
            scope=BaseSchema.parse(data.get("scope"), int),
            respect=BaseSchema.parse(data.get("respect"), int),
            payout=BaseSchema.parse(
                data.get("payout"), None | FactionCrimeRewardPayout
            ),
            money=BaseSchema.parse(data.get("money"), int),
            items=BaseSchema.parse(
                data.get("items"), typing.List[FactionCrimeRewardItem]
            ),
        )
