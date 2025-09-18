import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserRefillsResponse(BaseSchema):
    """
    JSON object of `UserRefillsResponse`.
    """

    refills: typing.TypedDict(
        "", {"token": bool, "special_count": int, "nerve": bool, "energy": bool}
    )

    @staticmethod
    def parse(data):
        return UserRefillsResponse(
            refills=BaseSchema.parse(
                data.get("refills"),
                typing.TypedDict(
                    "",
                    {
                        "token": bool,
                        "special_count": int,
                        "nerve": bool,
                        "energy": bool,
                    },
                ),
            ),
        )
