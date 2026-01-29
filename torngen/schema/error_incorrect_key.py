import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorIncorrectKey(BaseSchema):
    """
    JSON object of `ErrorIncorrectKey`.
    """

    error: str
    code: typing.Literal[2]

    @staticmethod
    def parse(data):
        return ErrorIncorrectKey(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[2]),
        )
