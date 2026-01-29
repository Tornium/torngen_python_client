import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorIncorrectId(BaseSchema):
    """
    JSON object of `ErrorIncorrectId`.
    """

    error: str
    code: typing.Literal[6]

    @staticmethod
    def parse(data):
        return ErrorIncorrectId(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[6]),
        )
