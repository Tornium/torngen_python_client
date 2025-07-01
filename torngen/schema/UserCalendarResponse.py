import typing

from UserCalendar import UserCalendar

from ..base_schema import BaseSchema


class UserCalendarResponse(BaseSchema):

    calendar: UserCalendar
