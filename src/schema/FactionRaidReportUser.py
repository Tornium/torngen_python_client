import typing

from UserId import UserId

from ..base_schema import BaseSchema


class FactionRaidReportUser(BaseSchema):

    name: str
    id: UserId
