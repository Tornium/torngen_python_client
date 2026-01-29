import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorApiKeyPaused(BaseSchema):
    """
    JSON object of `ErrorApiKeyPaused`.
    """

    error: str
    code: typing.Literal[18]

    @staticmethod
    def parse(data):
        return ErrorApiKeyPaused(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[18]),
        )
