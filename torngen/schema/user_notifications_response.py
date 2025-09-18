import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserNotificationsResponse(BaseSchema):
    """
    JSON object of `UserNotificationsResponse`.
    """

    notifications: typing.TypedDict(
        "", {"messages": int, "events": int, "competition": int, "awards": int}
    )

    @staticmethod
    def parse(data):
        return UserNotificationsResponse(
            notifications=BaseSchema.parse(
                data.get("notifications"),
                typing.TypedDict(
                    "",
                    {"messages": int, "events": int, "competition": int, "awards": int},
                ),
            ),
        )
