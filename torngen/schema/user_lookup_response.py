import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_selection_name import UserSelectionName


@dataclass
class UserLookupResponse(BaseSchema):
    """
    JSON object of `UserLookupResponse`.
    """

    selections: typing.List[UserSelectionName]

    @staticmethod
    def parse(data):
        return UserLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[UserSelectionName]
            ),
        )
