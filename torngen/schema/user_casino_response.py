import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCasinoResponse(BaseSchema):
    """
    JSON object of `UserCasinoResponse`.
    """

    casino: typing.TypedDict("", {"tokens": int, "streak": int})

    @staticmethod
    def parse(data):
        return UserCasinoResponse(
            casino=BaseSchema.parse(
                data.get("casino"), typing.TypedDict("", {"tokens": int, "streak": int})
            ),
        )
