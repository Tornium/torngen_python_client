import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsHospitalPopular(BaseSchema):
    """
    JSON object of `PersonalStatsHospitalPopular`.
    """

    hospital: typing.TypedDict(
        "",
        {
            "reviving": typing.TypedDict("", {"skill": int, "revives": int}),
            "medical_items_used": int,
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsHospitalPopular(
            hospital=BaseSchema.parse(
                data.get("hospital"),
                typing.TypedDict(
                    "",
                    {
                        "reviving": typing.TypedDict(
                            "", {"skill": int, "revives": int}
                        ),
                        "medical_items_used": int,
                    },
                ),
            ),
        )
