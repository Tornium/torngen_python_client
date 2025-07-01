import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_selection_name import ForumSelectionName


@dataclass
class ForumLookupResponse(BaseSchema):
    """
    JSON object of `ForumLookupResponse`.
    """

    selections: typing.List[ForumSelectionName]

    @staticmethod
    def parse(data):
        return ForumLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[ForumSelectionName]
            ),
        )
