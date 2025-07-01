import typing

from ..base_schema import BaseSchema


class PersonalStatsHospital(BaseSchema):

    hospital: typing.TypedDict(
        "",
        {
            "times_hospitalized": int,
            "reviving": typing.TypedDict(
                "", {"skill": int, "revives_received": int, "revives": int}
            ),
            "medical_items_used": int,
            "blood_withdrawn": int,
        },
    )
