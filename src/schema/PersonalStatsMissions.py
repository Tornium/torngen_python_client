import typing

from ..base_schema import BaseSchema


class PersonalStatsMissions(BaseSchema):

    missions: typing.TypedDict(
        "",
        {
            "missions": int,
            "credits": int,
            "contracts": typing.TypedDict("", {"total": int, "duke": int}),
        },
    )
