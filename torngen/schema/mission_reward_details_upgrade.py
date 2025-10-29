import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_mod_id import ItemModId


@dataclass
class MissionRewardDetailsUpgrade(BaseSchema):
    """
    JSON object of `MissionRewardDetailsUpgrade`.
    """

    name: str
    id: ItemModId

    @staticmethod
    def parse(data):
        return MissionRewardDetailsUpgrade(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemModId),
        )
