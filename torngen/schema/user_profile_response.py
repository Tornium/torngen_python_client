import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .honor_id import HonorId
from .profile_spouse import ProfileSpouse
from .property_id import PropertyId
from .user_donator_status_enum import UserDonatorStatusEnum
from .user_gender_enum import UserGenderEnum
from .user_id import UserId
from .user_last_action import UserLastAction
from .user_rank_enum import UserRankEnum
from .user_role_enum import UserRoleEnum
from .user_status import UserStatus
from .user_title_enum import UserTitleEnum


@dataclass
class UserProfileResponse(BaseSchema):
    """
    JSON object of `UserProfileResponse`.
    """

    profile: typing.TypedDict(
        "",
        {
            "title": UserTitleEnum,
            "status": UserStatus,
            "spouse": None | ProfileSpouse,
            "signed_up": int,
            "role": UserRoleEnum,
            "revivable": bool,
            "rank": UserRankEnum,
            "property": typing.TypedDict("", {"name": str, "id": PropertyId}),
            "name": str,
            "life": typing.TypedDict("", {"maximum": int, "current": int}),
            "level": int,
            "last_action": UserLastAction,
            "karma": int,
            "image": None | str,
            "id": UserId,
            "honor_id": HonorId,
            "gender": UserGenderEnum,
            "friends": int,
            "forum_posts": int,
            "faction_id": None | FactionId,
            "enemies": int,
            "donator_status": None | UserDonatorStatusEnum,
            "awards": int,
            "age": int,
        },
    )

    @staticmethod
    def parse(data):
        return UserProfileResponse(
            profile=BaseSchema.parse(
                data.get("profile"),
                typing.TypedDict(
                    "",
                    {
                        "title": UserTitleEnum,
                        "status": UserStatus,
                        "spouse": None | ProfileSpouse,
                        "signed_up": int,
                        "role": UserRoleEnum,
                        "revivable": bool,
                        "rank": UserRankEnum,
                        "property": typing.TypedDict(
                            "", {"name": str, "id": PropertyId}
                        ),
                        "name": str,
                        "life": typing.TypedDict("", {"maximum": int, "current": int}),
                        "level": int,
                        "last_action": UserLastAction,
                        "karma": int,
                        "image": None | str,
                        "id": UserId,
                        "honor_id": HonorId,
                        "gender": UserGenderEnum,
                        "friends": int,
                        "forum_posts": int,
                        "faction_id": None | FactionId,
                        "enemies": int,
                        "donator_status": None | UserDonatorStatusEnum,
                        "awards": int,
                        "age": int,
                    },
                ),
            ),
        )
