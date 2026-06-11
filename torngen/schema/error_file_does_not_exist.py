import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorFileDoesNotExist(BaseSchema):
    """
    JSON object of `ErrorFileDoesNotExist`.
    """

    error: str
    code: typing.Literal[30]

    @staticmethod
    def parse(data):
        return ErrorFileDoesNotExist(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[30]),
        )
