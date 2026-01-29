import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorApiDisabled(BaseSchema):
    """
    JSON object of `ErrorApiDisabled`.
    """

    error: str
    code: typing.Literal[9]

    @staticmethod
    def parse(data):
        return ErrorApiDisabled(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[9]),
        )
