import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorOnlyAvailableInApiV1(BaseSchema):
    """
    JSON object of `ErrorOnlyAvailableInApiV1`.
    """

    error: str
    code: typing.Literal[22]

    @staticmethod
    def parse(data):
        return ErrorOnlyAvailableInApiV1(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[22]),
        )
