import typing

from RacingSelectionName import RacingSelectionName

from ..base_schema import BaseSchema


class RacingLookupResponse(BaseSchema):

    selections: typing.List[RacingSelectionName]
