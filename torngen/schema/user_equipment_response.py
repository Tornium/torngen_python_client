import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_clothing import UserClothing
from .user_equipment import UserEquipment


@dataclass
class UserEquipmentResponse(BaseSchema):
    """
    JSON object of `UserEquipmentResponse`.
    """

    equipment: typing.List[UserEquipment]
    clothing: typing.List[UserClothing]

    @staticmethod
    def parse(data):
        return UserEquipmentResponse(
            equipment=BaseSchema.parse(
                data.get("equipment"), typing.List[UserEquipment]
            ),
            clothing=BaseSchema.parse(data.get("clothing"), typing.List[UserClothing]),
        )
