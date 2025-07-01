import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_selection_name import FactionSelectionName


@dataclass
class FactionLookupResponse(BaseSchema):
    """
    JSON object of `FactionLookupResponse`.
    """

    selections: typing.List[FactionSelectionName]

    @staticmethod
    def parse(data):
        return FactionLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[FactionSelectionName]
            ),
        )
