import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserOrganizedCrimeError(BaseSchema):
    """
    JSON object of `UserOrganizedCrimeError`.
    """

    error: str
    code: typing.Literal[27]

    @staticmethod
    def parse(data):
        return UserOrganizedCrimeError(
            error=BaseSchema.parse(data.get("error"), str),
            code=BaseSchema.parse(data.get("code"), typing.Literal[27]),
        )
