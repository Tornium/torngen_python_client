import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserHonorProgress(BaseSchema):
    """
    JSON object of `UserHonorProgress`.
    """

    target: int
    current: int

    @staticmethod
    def parse(data):
        return UserHonorProgress(
            target=BaseSchema.parse(data.get("target"), int),
            current=BaseSchema.parse(data.get("current"), int),
        )
