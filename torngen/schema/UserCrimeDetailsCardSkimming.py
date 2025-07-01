import typing

from ..base_schema import BaseSchema


class UserCrimeDetailsCardSkimming(BaseSchema):

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
