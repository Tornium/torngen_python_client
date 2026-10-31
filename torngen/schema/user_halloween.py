import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_halloween_basket_upgrade import UserHalloweenBasketUpgrade


@dataclass
class UserHalloween(BaseSchema):
    """
    JSON object of `UserHalloween`.
    """

    treats: typing.TypedDict("", {"total": int, "current": int})
    basket_upgrades: typing.List[UserHalloweenBasketUpgrade]

    @staticmethod
    def parse(data):
        return UserHalloween(
            treats=BaseSchema.parse(
                data.get("treats"), typing.TypedDict("", {"total": int, "current": int})
            ),
            basket_upgrades=BaseSchema.parse(
                data.get("basket_upgrades"), typing.List[UserHalloweenBasketUpgrade]
            ),
        )
