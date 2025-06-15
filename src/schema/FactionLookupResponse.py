import typing

from FactionSelectionName import FactionSelectionName

from ..base_schema import BaseSchema


class FactionLookupResponse(BaseSchema):

    selections: typing.List[FactionSelectionName]
