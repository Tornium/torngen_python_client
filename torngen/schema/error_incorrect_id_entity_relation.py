import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorIncorrectIdEntityRelation(BaseSchema):
    """
    JSON object of `ErrorIncorrectIdEntityRelation`.
    """

    error: str
    code: typing.Literal[7]

    @staticmethod
    def parse(data):
        return ErrorIncorrectIdEntityRelation(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[7]),
        )
