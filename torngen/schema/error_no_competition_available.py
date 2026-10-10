import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorNoCompetitionAvailable(BaseSchema):
    """
    JSON object of `ErrorNoCompetitionAvailable`.
    """

    error: str
    code: typing.Literal[33]

    @staticmethod
    def parse(data):
        return ErrorNoCompetitionAvailable(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[33]),
        )
