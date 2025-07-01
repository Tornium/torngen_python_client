import typing

from ..base_schema import BaseSchema


class PersonalStatsDrugs(BaseSchema):

    drugs: typing.TypedDict(
        "",
        {
            "xanax": int,
            "vicodin": int,
            "total": int,
            "speed": int,
            "shrooms": int,
            "rehabilitations": typing.TypedDict("", {"fees": int, "amount": int}),
            "pcp": int,
            "overdoses": int,
            "opium": int,
            "lsd": int,
            "ketamine": int,
            "ecstasy": int,
            "cannabis": int,
        },
    )
