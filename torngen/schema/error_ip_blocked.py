import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorIpBlocked(BaseSchema):
    """
    JSON object of `ErrorIpBlocked`.
    """

    error: str
    code: typing.Literal[8]

    @staticmethod
    def parse(data):
        return ErrorIpBlocked(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[8]),
        )
