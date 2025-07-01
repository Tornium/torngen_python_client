import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_selection_name import TornSelectionName


@dataclass
class TornLookupResponse(BaseSchema):
    """
    JSON object of `TornLookupResponse`.
    """

    selections: typing.List[TornSelectionName]

    @staticmethod
    def parse(data):
        return TornLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[TornSelectionName]
            ),
        )
