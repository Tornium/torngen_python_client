import typing

from ..base_schema import BaseSchema


class FactionNews(BaseSchema):

    timestamp: int
    text: str
    id: str
