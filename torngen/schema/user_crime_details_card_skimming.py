import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeDetailsCardSkimming(BaseSchema):
    """
    JSON object of `UserCrimeDetailsCardSkimming`.
    """

    skimmers: typing.TypedDict(
        "", {"oldest_recovered": int, "most_lucrative": int, "lost": int, "active": int}
    )
    card_details: typing.TypedDict(
        "",
        {
            "sold": int,
            "recovered": int,
            "recoverable": int,
            "lost": int,
            "areas": typing.List[typing.TypedDict("", {"id": int, "amount": int})],
        },
    )

    @staticmethod
    def parse(data):
        return UserCrimeDetailsCardSkimming(
            skimmers=BaseSchema.parse(
                data.get("skimmers"),
                typing.TypedDict(
                    "",
                    {
                        "oldest_recovered": int,
                        "most_lucrative": int,
                        "lost": int,
                        "active": int,
                    },
                ),
            ),
            card_details=BaseSchema.parse(
                data.get("card_details"),
                typing.TypedDict(
                    "",
                    {
                        "sold": int,
                        "recovered": int,
                        "recoverable": int,
                        "lost": int,
                        "areas": typing.List[
                            typing.TypedDict("", {"id": int, "amount": int})
                        ],
                    },
                ),
            ),
        )
