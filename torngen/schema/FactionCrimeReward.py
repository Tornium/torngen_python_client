import typing

from FactionCrimeRewardItem import FactionCrimeRewardItem
from FactionCrimeRewardPayout import FactionCrimeRewardPayout

from ..base_schema import BaseSchema


class FactionCrimeReward(BaseSchema):

    scope: int
    respect: int
    payout: None | FactionCrimeRewardPayout
    money: int
    items: typing.List[FactionCrimeRewardItem]
