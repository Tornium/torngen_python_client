import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorCityStatsCronFailed(BaseSchema):
    """
    JSON object of `ErrorCityStatsCronFailed`.
    """

    error: str
    code: typing.Literal[31]

    @staticmethod
    def parse(data):
        return ErrorCityStatsCronFailed(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[31]),
        )
