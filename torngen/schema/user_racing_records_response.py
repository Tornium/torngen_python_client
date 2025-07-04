import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .race_track_id import RaceTrackId


@dataclass
class UserRacingRecordsResponse(BaseSchema):
    """
    JSON object of `UserRacingRecordsResponse`.
    """

    racingrecords: typing.List[
        typing.TypedDict(
            "",
            {
                "track": typing.TypedDict("", {"name": str, "id": RaceTrackId}),
                "records": typing.List[
                    typing.TypedDict(
                        "", {"lap_time": int, "car_name": str, "car_id": ItemId}
                    )
                ],
            },
        )
    ]

    @staticmethod
    def parse(data):
        return UserRacingRecordsResponse(
            racingrecords=BaseSchema.parse(
                data.get("racingrecords"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "track": typing.TypedDict(
                                "", {"name": str, "id": RaceTrackId}
                            ),
                            "records": typing.List[
                                typing.TypedDict(
                                    "",
                                    {
                                        "lap_time": int,
                                        "car_name": str,
                                        "car_id": ItemId,
                                    },
                                )
                            ],
                        },
                    )
                ],
            ),
        )
