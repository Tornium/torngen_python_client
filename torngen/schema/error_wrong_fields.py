import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorWrongFields(BaseSchema):
    """
    JSON object of `ErrorWrongFields`.
    """

    error: str
    code: typing.Literal[4]

    @staticmethod
    def parse(data):
        return ErrorWrongFields(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[4]),
        )
