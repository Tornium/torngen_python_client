import typing

from TornSelectionName import TornSelectionName

from ..base_schema import BaseSchema


class TornLookupResponse(BaseSchema):

    selections: typing.List[TornSelectionName]
