import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorKeyEmpty(BaseSchema):
    """
    JSON object of `ErrorKeyEmpty`.
    """

    error: str
    code: typing.Literal[1]

    @staticmethod
    def parse(data):
        return ErrorKeyEmpty(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[1]),
        )
