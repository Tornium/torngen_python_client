import typing

from ..base_schema import BaseSchema


class PersonalStatsBounties(BaseSchema):

    bounties: typing.TypedDict(
        "",
        {
            "received": typing.TypedDict("", {"value": int, "amount": int}),
            "placed": typing.TypedDict("", {"value": int, "amount": int}),
            "collected": typing.TypedDict("", {"value": int, "amount": int}),
        },
    )
