import typing

from ..base_schema import BaseSchema


class PersonalStatsJail(BaseSchema):

    jail: typing.TypedDict(
        "",
        {
            "times_jailed": int,
            "busts": typing.TypedDict("", {"success": int, "fails": int}),
            "bails": typing.TypedDict("", {"fees": int, "amount": int}),
        },
    )
