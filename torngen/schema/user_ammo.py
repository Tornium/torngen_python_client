import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .ammo_id import AmmoId
from .user_ammo_type import UserAmmoType


@dataclass
class UserAmmo(BaseSchema):
    """
    JSON object of `UserAmmo`.
    """

    types: typing.List[UserAmmoType]
    name: str
    id: AmmoId

    @staticmethod
    def parse(data):
        return UserAmmo(
            types=BaseSchema.parse(data.get("types"), typing.List[UserAmmoType]),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), AmmoId),
        )
