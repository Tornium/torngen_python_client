import typing

from ..base_schema import BaseSchema


class PersonalStatsRacing(BaseSchema):

    racing: typing.TypedDict(
        "",
        {
            "skill": int,
            "races": typing.TypedDict("", {"won": int, "entered": int}),
            "points": int,
        },
    )
