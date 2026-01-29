import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorOnlyAvailableInApiV2(BaseSchema):
    """
    JSON object of `ErrorOnlyAvailableInApiV2`.
    """

    error: str
    code: typing.Literal[23]

    @staticmethod
    def parse(data):
        return ErrorOnlyAvailableInApiV2(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[23]),
        )
