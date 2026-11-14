import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .gym_id import GymId
from .user_unlocked_gym import UserUnlockedGym


@dataclass
class UserGymResponse(BaseSchema):
    """
    JSON object of `UserGymResponse`.
    """

    gym: typing.TypedDict(
        "", {"unlocked_gyms": typing.List[UserUnlockedGym], "name": str, "id": GymId}
    )

    @staticmethod
    def parse(data):
        return UserGymResponse(
            gym=BaseSchema.parse(
                data.get("gym"),
                typing.TypedDict(
                    "",
                    {
                        "unlocked_gyms": typing.List[UserUnlockedGym],
                        "name": str,
                        "id": GymId,
                    },
                ),
            ),
        )
