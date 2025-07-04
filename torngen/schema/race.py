import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .race_class_enum import RaceClassEnum
from .race_id import RaceId
from .race_status_enum import RaceStatusEnum
from .race_track_id import RaceTrackId
from .user_id import UserId


@dataclass
class Race(BaseSchema):
    """
    JSON object of `Race`.
    """

    track_id: RaceTrackId
    title: str
    status: RaceStatusEnum
    schedule: typing.TypedDict(
        "", {"start": int, "join_until": int, "join_from": int, "end": None | int}
    )
    requirements: typing.TypedDict(
        "",
        {
            "requires_stock_car": bool,
            "requires_password": bool,
            "join_fee": int,
            "driver_class": None | RaceClassEnum,
            "car_item_id": None | ItemId,
            "car_class": None | RaceClassEnum,
        },
    )
    participants: typing.TypedDict("", {"minimum": int, "maximum": int, "current": int})
    laps: int
    is_official: bool
    id: RaceId
    creator_id: UserId

    @staticmethod
    def parse(data):
        return Race(
            track_id=BaseSchema.parse(data.get("track_id"), RaceTrackId),
            title=BaseSchema.parse(data.get("title"), str),
            status=BaseSchema.parse(data.get("status"), RaceStatusEnum),
            schedule=BaseSchema.parse(
                data.get("schedule"),
                typing.TypedDict(
                    "",
                    {
                        "start": int,
                        "join_until": int,
                        "join_from": int,
                        "end": None | int,
                    },
                ),
            ),
            requirements=BaseSchema.parse(
                data.get("requirements"),
                typing.TypedDict(
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
            ),
            participants=BaseSchema.parse(
                data.get("participants"),
                typing.TypedDict("", {"minimum": int, "maximum": int, "current": int}),
            ),
            laps=BaseSchema.parse(data.get("laps"), int),
            is_official=BaseSchema.parse(data.get("is_official"), bool),
            id=BaseSchema.parse(data.get("id"), RaceId),
            creator_id=BaseSchema.parse(data.get("creator_id"), UserId),
        )
