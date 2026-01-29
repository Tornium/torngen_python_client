import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorMustMigrateToOrganizedCrimesV2(BaseSchema):
    """
    JSON object of `ErrorMustMigrateToOrganizedCrimesV2`.
    """

    error: str
    code: typing.Literal[27]

    @staticmethod
    def parse(data):
        return ErrorMustMigrateToOrganizedCrimesV2(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[27]),
        )
