import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_shoplifting import TornShoplifting


@dataclass
class TornShopliftingResponse(BaseSchema):
    """
    JSON object of `TornShopliftingResponse`.
    """

    shoplifting: typing.List[TornShoplifting]

    @staticmethod
    def parse(data):
        return TornShopliftingResponse(
            shoplifting=BaseSchema.parse(
                data.get("shoplifting"), typing.List[TornShoplifting]
            ),
        )
