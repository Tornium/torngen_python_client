import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorOnlyCategoryOrStatsAllowed(BaseSchema):
    """
    JSON object of `ErrorOnlyCategoryOrStatsAllowed`.
    """

    error: str
    code: typing.Literal[26]

    @staticmethod
    def parse(data):
        return ErrorOnlyCategoryOrStatsAllowed(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[26]),
        )
