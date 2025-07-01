import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsHospital(BaseSchema):
    """
    JSON object of `PersonalStatsHospital`.
    """

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

    @staticmethod
    def parse(data):
        return PersonalStatsHospital(
            hospital=BaseSchema.parse(
                data.get("hospital"),
                typing.TypedDict(
                    "",
                    {
                        "times_hospitalized": int,
                        "reviving": typing.TypedDict(
                            "", {"skill": int, "revives_received": int, "revives": int}
                        ),
                        "medical_items_used": int,
                        "blood_withdrawn": int,
                    },
                ),
            ),
        )
