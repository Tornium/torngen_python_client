import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .halloween_basket_upgrade_id import HalloweenBasketUpgradeId


@dataclass
class TornHalloweenUpgrade(BaseSchema):
    """
    JSON object of `TornHalloweenUpgrade`.
    """

    requirement: int
    name: str
    id: HalloweenBasketUpgradeId
    flavor: str
    description: str
    cost: int

    @staticmethod
    def parse(data):
        return TornHalloweenUpgrade(
            requirement=BaseSchema.parse(data.get("requirement"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), HalloweenBasketUpgradeId),
            flavor=BaseSchema.parse(data.get("flavor"), str),
            description=BaseSchema.parse(data.get("description"), str),
            cost=BaseSchema.parse(data.get("cost"), int),
        )
