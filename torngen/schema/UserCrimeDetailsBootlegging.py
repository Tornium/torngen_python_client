import typing

from ..base_schema import BaseSchema


class UserCrimeDetailsBootlegging(BaseSchema):

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
