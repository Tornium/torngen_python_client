import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorInvalidStatRequested(BaseSchema):
    """
    JSON object of `ErrorInvalidStatRequested`.
    """

    error: str
    code: typing.Literal[25]

    @staticmethod
    def parse(data):
        return ErrorInvalidStatRequested(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[25]),
        )
