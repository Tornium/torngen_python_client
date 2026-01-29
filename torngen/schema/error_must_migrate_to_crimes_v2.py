import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorMustMigrateToCrimesV2(BaseSchema):
    """
    JSON object of `ErrorMustMigrateToCrimesV2`.
    """

    error: str
    code: typing.Literal[19]

    @staticmethod
    def parse(data):
        return ErrorMustMigrateToCrimesV2(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[19]),
        )
