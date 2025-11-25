import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .discord_id import DiscordId
from .user_id import UserId


@dataclass
class UserDiscordResponse(BaseSchema):
    """
    JSON object of `UserDiscordResponse`.
    """

    discord: typing.TypedDict("", {"user_id": UserId, "discord_id": DiscordId})

    @staticmethod
    def parse(data):
        return UserDiscordResponse(
            discord=BaseSchema.parse(
                data.get("discord"),
                typing.TypedDict("", {"user_id": UserId, "discord_id": DiscordId}),
            ),
        )
