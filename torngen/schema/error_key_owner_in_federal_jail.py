import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorKeyOwnerInFederalJail(BaseSchema):
    """
    JSON object of `ErrorKeyOwnerInFederalJail`.
    """

    error: str
    code: typing.Literal[10]

    @staticmethod
    def parse(data):
        return ErrorKeyOwnerInFederalJail(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[10]),
        )
