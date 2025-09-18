import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCooldownsResponse(BaseSchema):
    """
    JSON object of `UserCooldownsResponse`.
    """

    cooldowns: typing.TypedDict("", {"medical": int, "drug": int, "booster": int})

    @staticmethod
    def parse(data):
        return UserCooldownsResponse(
            cooldowns=BaseSchema.parse(
                data.get("cooldowns"),
                typing.TypedDict("", {"medical": int, "drug": int, "booster": int}),
            ),
        )
