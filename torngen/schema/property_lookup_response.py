import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .property_selection_name import PropertySelectionName


@dataclass
class PropertyLookupResponse(BaseSchema):
    """
    JSON object of `PropertyLookupResponse`.
    """

    selections: typing.List[PropertySelectionName]

    @staticmethod
    def parse(data):
        return PropertyLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[PropertySelectionName]
            ),
        )
