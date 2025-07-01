import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_calendar import UserCalendar


@dataclass
class UserCalendarResponse(BaseSchema):
    """
    JSON object of `UserCalendarResponse`.
    """

    calendar: UserCalendar

    @staticmethod
    def parse(data):
        return UserCalendarResponse(
            calendar=BaseSchema.parse(data.get("calendar"), UserCalendar),
        )
