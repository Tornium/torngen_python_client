import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_weapon_exp import UserWeaponExp


@dataclass
class UserWeaponExpResponse(BaseSchema):
    """
    JSON object of `UserWeaponExpResponse`.
    """

    weaponexp: typing.List[UserWeaponExp]

    @staticmethod
    def parse(data):
        return UserWeaponExpResponse(
            weaponexp=BaseSchema.parse(
                data.get("weaponexp"), typing.List[UserWeaponExp]
            ),
        )
