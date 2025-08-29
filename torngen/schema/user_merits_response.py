import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_merits import UserMerits


@dataclass
class UserMeritsResponse(BaseSchema):
    """
    JSON object of `UserMeritsResponse`.
    """

    merits: UserMerits

    @staticmethod
    def parse(data):
        return UserMeritsResponse(
            merits=BaseSchema.parse(data.get("merits"), UserMerits),
        )
