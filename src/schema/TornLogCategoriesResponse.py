import typing

from TornLogCategory import TornLogCategory

from ..base_schema import BaseSchema


class TornLogCategoriesResponse(BaseSchema):

    logcategories: typing.List[TornLogCategory]
