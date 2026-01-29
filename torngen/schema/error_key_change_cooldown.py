import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorKeyChangeCooldown(BaseSchema):
    """
    JSON object of `ErrorKeyChangeCooldown`.
    """

    error: str
    code: typing.Literal[11]

    @staticmethod
    def parse(data):
        return ErrorKeyChangeCooldown(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[11]),
        )
