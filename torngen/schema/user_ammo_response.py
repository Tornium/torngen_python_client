import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_ammo import UserAmmo


@dataclass
class UserAmmoResponse(BaseSchema):
    """
    JSON object of `UserAmmoResponse`.
    """

    ammo: typing.Optional[typing.List[UserAmmo]]

    @staticmethod
    def parse(data):
        return UserAmmoResponse(
            ammo=BaseSchema.parse(
                data.get("ammo"), typing.Optional[typing.List[UserAmmo]]
            ),
        )
