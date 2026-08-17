import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .gym_id import GymId


@dataclass
class UserGymResponse(BaseSchema):
    """
    JSON object of `UserGymResponse`.
    """

    gym: typing.TypedDict("", {"name": str, "id": GymId})

    @staticmethod
    def parse(data):
        return UserGymResponse(
            gym=BaseSchema.parse(
                data.get("gym"), typing.TypedDict("", {"name": str, "id": GymId})
            ),
        )
