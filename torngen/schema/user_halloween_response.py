import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_halloween import UserHalloween


@dataclass
class UserHalloweenResponse(BaseSchema):
    """
    JSON object of `UserHalloweenResponse`.
    """

    halloween: UserHalloween

    @staticmethod
    def parse(data):
        return UserHalloweenResponse(
            halloween=BaseSchema.parse(data.get("halloween"), UserHalloween),
        )
