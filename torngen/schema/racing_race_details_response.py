import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .race_class_enum import RaceClassEnum
from .race_id import RaceId
from .race_status_enum import RaceStatusEnum
from .race_track_id import RaceTrackId
from .racer_details import RacerDetails
from .user_id import UserId


@dataclass
class RacingRaceDetailsResponse(BaseSchema):
    """
    JSON object of `RacingRaceDetailsResponse`.
    """

    race: typing.TypedDict(
        "",
        {
            "results": typing.List[RacerDetails],
            "is_official": bool,
            "track_id": RaceTrackId,
            "title": str,
            "status": RaceStatusEnum,
            "schedule": typing.TypedDict(
                "",
                {"start": int, "join_until": int, "join_from": int, "end": None | int},
            ),
            "requirements": typing.TypedDict(
                "",
                {
                    "requires_stock_car": bool,
                    "requires_password": bool,
                    "join_fee": int,
                    "driver_class": None | RaceClassEnum,
                    "car_item_id": None | ItemId,
                    "car_class": None | RaceClassEnum,
                },
            ),
            "participants": typing.TypedDict(
                "", {"minimum": int, "maximum": int, "current": int}
            ),
            "laps": int,
            "is_official": bool,
            "id": RaceId,
            "creator_id": UserId,
        },
    )

    @staticmethod
    def parse(data):
        return RacingRaceDetailsResponse(
            race=BaseSchema.parse(
                data.get("race"),
                typing.TypedDict(
                    "",
                    {
                        "results": typing.List[RacerDetails],
                        "is_official": bool,
                        "track_id": RaceTrackId,
                        "title": str,
                        "status": RaceStatusEnum,
                        "schedule": typing.TypedDict(
                            "",
                            {
                                "start": int,
                                "join_until": int,
                                "join_from": int,
                                "end": None | int,
                            },
                        ),
                        "requirements": typing.TypedDict(
                            "",
                            {
                                "requires_stock_car": bool,
                                "requires_password": bool,
                                "join_fee": int,
                                "driver_class": None | RaceClassEnum,
                                "car_item_id": None | ItemId,
                                "car_class": None | RaceClassEnum,
                            },
                        ),
                        "participants": typing.TypedDict(
                            "", {"minimum": int, "maximum": int, "current": int}
                        ),
                        "laps": int,
                        "is_official": bool,
                        "id": RaceId,
                        "creator_id": UserId,
                    },
                ),
            ),
        )
