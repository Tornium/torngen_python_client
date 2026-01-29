import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorKeyReadError(BaseSchema):
    """
    JSON object of `ErrorKeyReadError`.
    """

    error: str
    code: typing.Literal[12]

    @staticmethod
    def parse(data):
        return ErrorKeyReadError(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[12]),
        )
