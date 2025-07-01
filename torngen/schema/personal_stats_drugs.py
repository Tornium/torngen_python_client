import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsDrugs(BaseSchema):
    """
    JSON object of `PersonalStatsDrugs`.
    """

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

    @staticmethod
    def parse(data):
        return PersonalStatsDrugs(
            drugs=BaseSchema.parse(
                data.get("drugs"),
                typing.TypedDict(
                    "",
                    {
                        "xanax": int,
                        "vicodin": int,
                        "total": int,
                        "speed": int,
                        "shrooms": int,
                        "rehabilitations": typing.TypedDict(
                            "", {"fees": int, "amount": int}
                        ),
                        "pcp": int,
                        "overdoses": int,
                        "opium": int,
                        "lsd": int,
                        "ketamine": int,
                        "ecstasy": int,
                        "cannabis": int,
                    },
                ),
            ),
        )
