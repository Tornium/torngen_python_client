import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorTooManyRequests(BaseSchema):
    """
    JSON object of `ErrorTooManyRequests`.
    """

    error: str
    code: typing.Literal[5]

    @staticmethod
    def parse(data):
        return ErrorTooManyRequests(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[5]),
        )
