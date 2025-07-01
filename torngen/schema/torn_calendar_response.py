import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_calendar_activity import TornCalendarActivity


@dataclass
class TornCalendarResponse(BaseSchema):
    """
    JSON object of `TornCalendarResponse`.
    """

    calendar: typing.TypedDict(
        "",
        {
            "events": typing.List[TornCalendarActivity],
            "competitions": typing.List[TornCalendarActivity],
        },
    )

    @staticmethod
    def parse(data):
        return TornCalendarResponse(
            calendar=BaseSchema.parse(
                data.get("calendar"),
                typing.TypedDict(
                    "",
                    {
                        "events": typing.List[TornCalendarActivity],
                        "competitions": typing.List[TornCalendarActivity],
                    },
                ),
            ),
        )
