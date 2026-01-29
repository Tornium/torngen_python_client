import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorKeyTemporaryDisabled(BaseSchema):
    """
    JSON object of `ErrorKeyTemporaryDisabled`.
    """

    error: str
    code: typing.Literal[13]

    @staticmethod
    def parse(data):
        return ErrorKeyTemporaryDisabled(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[13]),
        )
