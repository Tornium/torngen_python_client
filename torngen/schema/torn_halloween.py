import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_halloween_upgrade import TornHalloweenUpgrade


@dataclass
class TornHalloween(BaseSchema):
    """
    JSON object of `TornHalloween`.
    """

    basket_upgrades: typing.List[TornHalloweenUpgrade]

    @staticmethod
    def parse(data):
        return TornHalloween(
            basket_upgrades=BaseSchema.parse(
                data.get("basket_upgrades"), typing.List[TornHalloweenUpgrade]
            ),
        )
