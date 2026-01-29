import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorIncorrectLogId(BaseSchema):
    """
    JSON object of `ErrorIncorrectLogId`.
    """

    error: str
    code: typing.Literal[28]

    @staticmethod
    def parse(data):
        return ErrorIncorrectLogId(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[28]),
        )
