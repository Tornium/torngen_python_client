import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorRaceNotFinished(BaseSchema):
    """
    JSON object of `ErrorRaceNotFinished`.
    """

    error: str
    code: typing.Literal[20]

    @staticmethod
    def parse(data):
        return ErrorRaceNotFinished(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[20]),
        )
