import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorIncorrectCategory(BaseSchema):
    """
    JSON object of `ErrorIncorrectCategory`.
    """

    error: str
    code: typing.Literal[21]

    @staticmethod
    def parse(data):
        return ErrorIncorrectCategory(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[21]),
        )
