import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsCommunication(BaseSchema):
    """
    JSON object of `PersonalStatsCommunication`.
    """

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

    @staticmethod
    def parse(data):
        return PersonalStatsCommunication(
            communication=BaseSchema.parse(
                data.get("communication"),
                typing.TypedDict(
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
                ),
            ),
        )
