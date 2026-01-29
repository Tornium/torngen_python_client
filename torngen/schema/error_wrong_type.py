import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorWrongType(BaseSchema):
    """
    JSON object of `ErrorWrongType`.
    """

    error: str
    code: typing.Literal[3]

    @staticmethod
    def parse(data):
        return ErrorWrongType(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[3]),
        )
