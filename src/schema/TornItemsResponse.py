import typing

from TornItem import TornItem

from ..base_schema import BaseSchema


class TornItemsResponse(BaseSchema):

    items: typing.List[TornItem]
