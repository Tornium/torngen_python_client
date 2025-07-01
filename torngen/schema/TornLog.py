import typing

from LogId import LogId

from ..base_schema import BaseSchema


class TornLog(BaseSchema):

    title: str
    id: LogId
