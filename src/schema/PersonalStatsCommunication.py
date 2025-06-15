import typing

from ..base_schema import BaseSchema


class PersonalStatsCommunication(BaseSchema):

    communication: typing.TypedDict(
        "",
        {
            "personals": int,
            "mails_sent": typing.TypedDict(
                "",
                {
                    "total": int,
                    "spouse": int,
                    "friends": int,
                    "faction": int,
                    "colleagues": int,
                },
            ),
            "classified_ads": int,
        },
    )
