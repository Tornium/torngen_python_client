import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_mod_id import ItemModId
from .item_uid import ItemUid


@dataclass
class UserItemMod(BaseSchema):
    """
    JSON object of `UserItemMod`.
    """

    title: str
    id: ItemModId
    equipped_item_uid: None | ItemUid
    equipped: bool

    @staticmethod
    def parse(data):
        return UserItemMod(
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), ItemModId),
            equipped_item_uid=BaseSchema.parse(
                data.get("equipped_item_uid"), None | ItemUid
            ),
            equipped=BaseSchema.parse(data.get("equipped"), bool),
        )
