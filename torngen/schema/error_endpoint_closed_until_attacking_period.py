import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ErrorEndpointClosedUntilAttackingPeriod(BaseSchema):
    """
    JSON object of `ErrorEndpointClosedUntilAttackingPeriod`.
    """

    error: str
    code: typing.Literal[32]

    @staticmethod
    def parse(data):
        return ErrorEndpointClosedUntilAttackingPeriod(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[32]),
        )
