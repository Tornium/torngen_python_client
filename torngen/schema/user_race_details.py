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
class UserRaceDetails(BaseSchema):

    skill_gain: typing.Any

    @staticmethod
    def parse(data):
        return UserRaceDetails(
            skill_gain=BaseSchema.parse(data.get("skill_gain"), typing.Any),
        )
