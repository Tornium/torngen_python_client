import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeDetailsBootlegging(BaseSchema):
    """
    JSON object of `UserCrimeDetailsBootlegging`.
    """

    online_store: typing.TypedDict(
        "", {"visits": int, "sales": int, "earnings": int, "customers": int}
    )
    dvds_copied: int
    dvd_sales: typing.TypedDict(
        "",
        {
            "total": int,
            "thriller": int,
            "sci_fi": int,
            "romance": int,
            "horror": int,
            "fantasy": int,
            "earnings": int,
            "drama": int,
            "comedy": int,
            "action": int,
        },
    )

    @staticmethod
    def parse(data):
        return UserCrimeDetailsBootlegging(
            online_store=BaseSchema.parse(
                data.get("online_store"),
                typing.TypedDict(
                    "", {"visits": int, "sales": int, "earnings": int, "customers": int}
                ),
            ),
            dvds_copied=BaseSchema.parse(data.get("dvds_copied"), int),
            dvd_sales=BaseSchema.parse(
                data.get("dvd_sales"),
                typing.TypedDict(
                    "",
                    {
                        "total": int,
                        "thriller": int,
                        "sci_fi": int,
                        "romance": int,
                        "horror": int,
                        "fantasy": int,
                        "earnings": int,
                        "drama": int,
                        "comedy": int,
                        "action": int,
                    },
                ),
            ),
        )
