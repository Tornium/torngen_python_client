import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorDailyReadLimitReached(BaseSchema):
    """
    JSON object of `ErrorDailyReadLimitReached`.
    """

    error: str
    code: typing.Literal[14]

    @staticmethod
    def parse(data):
        return ErrorDailyReadLimitReached(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[14]),
        )
