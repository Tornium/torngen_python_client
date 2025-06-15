import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class ReportHistoryFaction(BaseSchema):

    name: str
    left: None | str
    joined: str
    id: FactionId
