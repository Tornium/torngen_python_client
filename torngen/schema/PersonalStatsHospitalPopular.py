import typing

from ..base_schema import BaseSchema


class PersonalStatsHospitalPopular(BaseSchema):

    hospital: typing.TypedDict(
        "",
        {
            "reviving": typing.TypedDict("", {"skill": int, "revives": int}),
            "medical_items_used": int,
        },
    )
