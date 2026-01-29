import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorAccessLevelTooLow(BaseSchema):
    """
    JSON object of `ErrorAccessLevelTooLow`.
    """

    error: str
    code: typing.Literal[16]

    @staticmethod
    def parse(data):
        return ErrorAccessLevelTooLow(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[16]),
        )
