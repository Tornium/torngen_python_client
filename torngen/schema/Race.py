import typing

from ItemId import ItemId
from RaceClassEnum import RaceClassEnum
from RaceId import RaceId
from RaceStatusEnum import RaceStatusEnum
from RaceTrackId import RaceTrackId
from UserId import UserId

from ..base_schema import BaseSchema


class Race(BaseSchema):

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
    id: RaceId
    creator_id: UserId
