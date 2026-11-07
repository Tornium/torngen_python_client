import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .halloween_basket_upgrade_id import HalloweenBasketUpgradeId


@dataclass
class UserHalloweenBasketUpgrade(BaseSchema):
    """
    JSON object of `UserHalloweenBasketUpgrade`.
    """

    timestamp: int
    id: HalloweenBasketUpgradeId

    @staticmethod
    def parse(data):
        return UserHalloweenBasketUpgrade(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            id=BaseSchema.parse(data.get("id"), HalloweenBasketUpgradeId),
        )
