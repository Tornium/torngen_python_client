import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserStatus(BaseSchema):
    """
    JSON object of `UserStatus`.
    """

    until: None | int
    travel_type: str
    state: str
    details: None | str
    description: str

    @staticmethod
    def parse(data):
        return UserStatus(
            until=BaseSchema.parse(data.get("until"), None | int),
            travel_type=BaseSchema.parse(data.get("travel_type"), str),
            state=BaseSchema.parse(data.get("state"), str),
            details=BaseSchema.parse(data.get("details"), None | str),
            description=BaseSchema.parse(data.get("description"), str),
        )
