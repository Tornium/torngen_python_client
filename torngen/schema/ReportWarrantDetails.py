import typing

from UserId import UserId

from ..base_schema import BaseSchema


class ReportWarrantDetails(BaseSchema):

    warrant: int
    name: str
    id: UserId
