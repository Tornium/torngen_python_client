import typing

from TornCalendarActivity import TornCalendarActivity

from ..base_schema import BaseSchema


class TornCalendarResponse(BaseSchema):

    calendar: typing.TypedDict(
        "",
        {
            "events": typing.List[TornCalendarActivity],
            "competitions": typing.List[TornCalendarActivity],
        },
    )
