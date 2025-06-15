import typing

from ..base_schema import BaseSchema


class TornCalendarActivity(BaseSchema):

    title: str
    start: int
    end: int
    description: str
