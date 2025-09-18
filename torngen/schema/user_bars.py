import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_ongoing_chain import FactionOngoingChain
from .user_bar import UserBar


@dataclass
class UserBars(BaseSchema):
    """
    JSON object of `UserBars`.
    """

    nerve: UserBar
    life: UserBar
    happy: UserBar
    energy: UserBar
    chain: None | FactionOngoingChain

    @staticmethod
    def parse(data):
        return UserBars(
            nerve=BaseSchema.parse(data.get("nerve"), UserBar),
            life=BaseSchema.parse(data.get("life"), UserBar),
            happy=BaseSchema.parse(data.get("happy"), UserBar),
            energy=BaseSchema.parse(data.get("energy"), UserBar),
            chain=BaseSchema.parse(data.get("chain"), None | FactionOngoingChain),
        )
