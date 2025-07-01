import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .racing_selection_name import RacingSelectionName


@dataclass
class RacingLookupResponse(BaseSchema):
    """
    JSON object of `RacingLookupResponse`.
    """

    selections: typing.List[RacingSelectionName]

    @staticmethod
    def parse(data):
        return RacingLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[RacingSelectionName]
            ),
        )
