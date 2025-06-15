import typing

from ..base_schema import BaseSchema


class RequestLinks(BaseSchema):

    prev: None | str
    next: None | str
