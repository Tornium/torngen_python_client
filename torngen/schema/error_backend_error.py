import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorBackendError(BaseSchema):
    """
    JSON object of `ErrorBackendError`.
    """

    error: str
    code: typing.Literal[17]

    @staticmethod
    def parse(data):
        return ErrorBackendError(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[17]),
        )
