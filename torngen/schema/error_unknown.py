import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorUnknown(BaseSchema):
    """
    JSON object of `ErrorUnknown`.
    """

    error: str
    code: typing.Literal[0]

    @staticmethod
    def parse(data):
        return ErrorUnknown(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[0]),
        )
