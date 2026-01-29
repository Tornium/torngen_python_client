import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorLogUnavailable(BaseSchema):
    """
    JSON object of `ErrorLogUnavailable`.
    """

    error: str
    code: typing.Literal[15]

    @staticmethod
    def parse(data):
        return ErrorLogUnavailable(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[15]),
        )
