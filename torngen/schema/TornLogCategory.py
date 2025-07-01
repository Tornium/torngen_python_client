import typing

from LogCategoryId import LogCategoryId

from ..base_schema import BaseSchema


class TornLogCategory(BaseSchema):

    title: str
    id: LogCategoryId
